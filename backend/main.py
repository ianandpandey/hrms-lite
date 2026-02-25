from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import date
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os
import re
from contextlib import asynccontextmanager

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = "hrms_lite"

db_client = None
db = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global db_client, db
    db_client = AsyncIOMotorClient(MONGODB_URL)
    db = db_client[DATABASE_NAME]
    yield
    db_client.close()

app = FastAPI(title="HRMS Lite API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Employee(BaseModel):
    employee_id: str = Field(..., min_length=1)
    full_name: str = Field(..., min_length=1)
    email: str = Field(..., min_length=1)
    department: str = Field(..., min_length=1)
    
    @validator('email')
    def validate_email(cls, v):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, v):
            raise ValueError('Invalid email format')
        return v

class EmployeeResponse(Employee):
    id: str

class AttendanceRecord(BaseModel):
    employee_id: str = Field(..., min_length=1)
    date: date
    status: str = Field(..., pattern="^(Present|Absent)$")

class AttendanceResponse(AttendanceRecord):
    id: str

@app.get("/")
async def root():
    return {"message": "HRMS Lite API", "status": "running"}

@app.post("/api/employees", response_model=EmployeeResponse, status_code=201)
async def create_employee(employee: Employee):
    existing = await db.employees.find_one({"employee_id": employee.employee_id})
    if existing:
        raise HTTPException(status_code=400, detail="Employee ID already exists")
    
    existing_email = await db.employees.find_one({"email": employee.email})
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    result = await db.employees.insert_one(employee.dict())
    created = await db.employees.find_one({"_id": result.inserted_id})
    created["id"] = str(created["_id"])
    return created

@app.get("/api/employees", response_model=List[EmployeeResponse])
async def get_employees():
    employees = []
    async for emp in db.employees.find():
        emp["id"] = str(emp["_id"])
        employees.append(emp)
    return employees

@app.delete("/api/employees/{employee_id}", status_code=204)
async def delete_employee(employee_id: str):
    result = await db.employees.delete_one({"employee_id": employee_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    await db.attendance.delete_many({"employee_id": employee_id})
    return None

@app.post("/api/attendance", response_model=AttendanceResponse, status_code=201)
async def mark_attendance(attendance: AttendanceRecord):
    employee = await db.employees.find_one({"employee_id": attendance.employee_id})
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    existing = await db.attendance.find_one({
        "employee_id": attendance.employee_id,
        "date": attendance.date.isoformat()
    })
    if existing:
        raise HTTPException(status_code=400, detail="Attendance already marked for this date")
    
    record = attendance.dict()
    record["date"] = attendance.date.isoformat()
    result = await db.attendance.insert_one(record)
    created = await db.attendance.find_one({"_id": result.inserted_id})
    created["id"] = str(created["_id"])
    created["date"] = attendance.date
    return created

@app.get("/api/attendance/{employee_id}", response_model=List[AttendanceResponse])
async def get_attendance(employee_id: str):
    employee = await db.employees.find_one({"employee_id": employee_id})
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    records = []
    async for record in db.attendance.find({"employee_id": employee_id}).sort("date", -1):
        record["id"] = str(record["_id"])
        records.append(record)
    return records

@app.get("/api/attendance", response_model=List[AttendanceResponse])
async def get_all_attendance():
    records = []
    async for record in db.attendance.find().sort("date", -1):
        record["id"] = str(record["_id"])
        records.append(record)
    return records
