# HRMS Lite

A lightweight Human Resource Management System for managing employees and tracking daily attendance.

## 🚀 Live Demo

- **Frontend**: [Deploy on Vercel and add URL here]
- **Backend API**: [Deploy on Render and add URL here]
- **GitHub Repository**: https://github.com/[your-username]/hrms-lite

## 📋 Features

### Employee Management
- ✅ Add new employees with unique Employee ID
- ✅ View all employees in a clean table
- ✅ Delete employees
- ✅ Email validation
- ✅ Duplicate employee ID prevention

### Attendance Management
- ✅ Mark daily attendance (Present/Absent)
- ✅ View attendance records
- ✅ Filter attendance by employee
- ✅ Prevent duplicate attendance for same date

### UI/UX
- ✅ Clean, minimal, professional interface
- ✅ Loading states
- ✅ Empty states
- ✅ Error handling with user-friendly messages
- ✅ Responsive design

## 🛠️ Tech Stack

### Frontend
- **React** - UI library
- **Vite** - Build tool
- **TailwindCSS** - Styling
- **Axios** - HTTP client

### Backend
- **FastAPI** - Python web framework
- **Motor** - Async MongoDB driver
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

### Database
- **MongoDB** - NoSQL database (MongoDB Atlas for production)

### Deployment
- **Vercel** - Frontend hosting
- **Render** - Backend hosting

## 📦 Installation & Setup

### Prerequisites
- Node.js (v18+)
- Python (v3.9+)
- MongoDB (local or MongoDB Atlas)

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```bash
cp .env.example .env
```

5. Update `.env` with your MongoDB URL:
```
MONGODB_URL=mongodb://localhost:27017
# Or use MongoDB Atlas:
# MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/
```

6. Run the server:
```bash
uvicorn main:app --reload
```

Backend will run at `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create `.env` file:
```bash
cp .env.example .env
```

4. Update `.env` with backend URL:
```
VITE_API_URL=http://localhost:8000
```

5. Run the development server:
```bash
npm run dev
```

Frontend will run at `http://localhost:5173`

## 🚢 Deployment Guide

### Deploy Backend to Render

1. Create account on [Render](https://render.com)
2. Create new **Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variable:
   - `MONGODB_URL`: Your MongoDB Atlas connection string
6. Deploy!

### Deploy Frontend to Vercel

1. Create account on [Vercel](https://vercel.com)
2. Import your GitHub repository
3. Configure:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
4. Add environment variable:
   - `VITE_API_URL`: Your Render backend URL
5. Deploy!

### MongoDB Atlas Setup

1. Create free account on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a new cluster (free tier)
3. Create database user
4. Whitelist IP: `0.0.0.0/0` (allow from anywhere)
5. Get connection string and use in backend `.env`

## 📝 API Documentation

Once backend is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### API Endpoints

#### Employees
- `GET /api/employees` - Get all employees
- `POST /api/employees` - Create new employee
- `DELETE /api/employees/{employee_id}` - Delete employee

#### Attendance
- `GET /api/attendance` - Get all attendance records
- `GET /api/attendance/{employee_id}` - Get attendance for specific employee
- `POST /api/attendance` - Mark attendance

## 🧪 Testing the Application

1. Start both backend and frontend servers
2. Open `http://localhost:5173` in browser
3. Add a test employee:
   - Employee ID: EMP001
   - Name: John Doe
   - Email: john@example.com
   - Department: Engineering
4. Go to Attendance tab
5. Mark attendance for the employee
6. Verify records are displayed correctly

## 🎯 Project Structure

```
greenRider/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   ├── .env.example        # Environment template
│   └── render.yaml         # Render deployment config
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Employees.jsx
│   │   │   └── Attendance.jsx
│   │   ├── api.js          # API client
│   │   ├── App.jsx         # Main component
│   │   └── index.css       # Tailwind styles
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── vercel.json         # Vercel deployment config
└── README.md
```

## ⚠️ Assumptions & Limitations

- Single admin user (no authentication required as per requirements)
- No edit functionality for employees (only add/delete)
- No edit/delete for attendance records
- Attendance can only be marked once per employee per day
- No payroll or leave management features
- No advanced reporting or analytics

## 🔒 Security Notes

For production deployment:
- Use environment variables for sensitive data
- Enable CORS only for your frontend domain
- Use MongoDB Atlas with proper authentication
- Consider adding rate limiting
- Add authentication if needed in future

## 📧 Support

For issues or questions, please open an issue on GitHub.

## 📄 License

MIT License - feel free to use this project for learning or portfolio purposes.

---

**Built with ❤️ for HRMS Lite Assignment**
