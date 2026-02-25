# 🚀 Complete Deployment Guide - HRMS Lite

This guide will walk you through deploying your HRMS Lite application from scratch. Follow these steps in order.

**Total Time Required: ~30 minutes**

---

## 📋 Prerequisites Checklist

Before starting, make sure you have:
- [ ] GitHub account
- [ ] Git installed on your machine
- [ ] Application running locally (both frontend and backend)

---

## Step 1: Setup MongoDB Atlas (Database) ⏱️ 5 minutes

### 1.1 Create MongoDB Atlas Account

1. Go to [https://www.mongodb.com/cloud/atlas/register](https://www.mongodb.com/cloud/atlas/register)
2. Sign up with Google/GitHub or create new account
3. Complete email verification if required

### 1.2 Create a Free Cluster

1. After login, click **"Build a Database"** or **"Create"**
2. Choose **FREE** tier (M0 Sandbox)
3. Select a cloud provider (AWS recommended)
4. Choose a region closest to you
5. Cluster Name: `hrms-lite-cluster` (or keep default)
6. Click **"Create Cluster"** (takes 3-5 minutes to provision)

### 1.3 Create Database User

1. On the left sidebar, click **"Database Access"** under Security
2. Click **"Add New Database User"**
3. Authentication Method: **Password**
4. Username: `hrms_admin` (or your choice)
5. Password: Click **"Autogenerate Secure Password"** and **COPY IT**
   - ⚠️ **IMPORTANT**: Save this password somewhere safe!
6. Database User Privileges: **"Read and write to any database"**
7. Click **"Add User"**

### 1.4 Configure Network Access

1. On the left sidebar, click **"Network Access"** under Security
2. Click **"Add IP Address"**
3. Click **"Allow Access from Anywhere"**
   - This adds `0.0.0.0/0` (required for Render deployment)
4. Click **"Confirm"**

### 1.5 Get Connection String

1. Go back to **"Database"** (left sidebar)
2. Click **"Connect"** button on your cluster
3. Choose **"Connect your application"**
4. Driver: **Python**, Version: **3.12 or later**
5. Copy the connection string (looks like):
   ```
   mongodb+srv://hrms_admin:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
   ```
6. Replace `<password>` with the actual password you saved earlier
7. **Save this complete connection string** - you'll need it for Render

**Example final connection string:**
```
mongodb+srv://hrms_admin:MySecurePass123@cluster0.abc123.mongodb.net/?retryWrites=true&w=majority
```

✅ **MongoDB Atlas Setup Complete!**

---

## Step 2: Create GitHub Repository ⏱️ 5 minutes

### 2.1 Create New Repository

1. Go to [https://github.com/new](https://github.com/new)
2. Repository name: `hrms-lite` (or your choice)
3. Description: `Lightweight HRMS application with employee and attendance management`
4. Visibility: **Public** ⚠️ (Required for assignment)
5. **DO NOT** initialize with README, .gitignore, or license
6. Click **"Create repository"**

### 2.2 Push Your Code

Open terminal in your project directory and run:

```bash
cd /Users/anandpandey/Desktop/interview-projects/greenRider

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: HRMS Lite application"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/hrms-lite.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 2.3 Verify Upload

1. Refresh your GitHub repository page
2. You should see all your files uploaded
3. Verify both `backend/` and `frontend/` folders are present

✅ **GitHub Repository Created!**

---

## Step 3: Deploy Backend to Render ⏱️ 10 minutes

### 3.1 Create Render Account

1. Go to [https://render.com](https://render.com)
2. Click **"Get Started"** or **"Sign Up"**
3. Sign up with GitHub (recommended for easy integration)
4. Authorize Render to access your GitHub

### 3.2 Create New Web Service

1. From Render Dashboard, click **"New +"** → **"Web Service"**
2. Connect your GitHub repository:
   - If not connected, click **"Connect account"** → **GitHub**
   - Find and select your `hrms-lite` repository
   - Click **"Connect"**

### 3.3 Configure Web Service

Fill in the following settings:

**Basic Settings:**
- **Name**: `hrms-lite-backend` (or your choice)
- **Region**: Choose closest to you (e.g., Oregon, Frankfurt, Singapore)
- **Branch**: `main`
- **Root Directory**: `backend` ⚠️ **IMPORTANT**
- **Runtime**: `Python 3`

**Build & Deploy:**
- **Build Command**: 
  ```bash
  pip install -r requirements.txt
  ```
- **Start Command**: 
  ```bash
  uvicorn main:app --host 0.0.0.0 --port $PORT
  ```

**Instance Type:**
- Select **"Free"** tier

### 3.4 Add Environment Variables

Scroll down to **"Environment Variables"** section:

1. Click **"Add Environment Variable"**
2. Key: `MONGODB_URL`
3. Value: Paste your MongoDB Atlas connection string from Step 1.5
   ```
   mongodb+srv://hrms_admin:YourPassword@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
   ```

### 3.5 Deploy

1. Click **"Create Web Service"** at the bottom
2. Wait for deployment (takes 3-5 minutes)
3. Watch the logs - you should see:
   ```
   INFO:     Uvicorn running on http://0.0.0.0:10000
   INFO:     Application startup complete.
   ```

### 3.6 Get Backend URL

1. Once deployed, you'll see a green **"Live"** badge
2. Copy your backend URL (looks like):
   ```
   https://hrms-lite-backend.onrender.com
   ```
3. **Save this URL** - you'll need it for frontend deployment

### 3.7 Test Backend API

1. Open your backend URL in browser: `https://hrms-lite-backend.onrender.com`
2. You should see: `{"message":"HRMS Lite API","status":"running"}`
3. Test API docs: `https://hrms-lite-backend.onrender.com/docs`

✅ **Backend Deployed Successfully!**

---

## Step 4: Deploy Frontend to Vercel ⏱️ 5 minutes

### 4.1 Create Vercel Account

1. Go to [https://vercel.com/signup](https://vercel.com/signup)
2. Click **"Continue with GitHub"**
3. Authorize Vercel to access your GitHub

### 4.2 Import Project

1. From Vercel Dashboard, click **"Add New..."** → **"Project"**
2. Find your `hrms-lite` repository
3. Click **"Import"**

### 4.3 Configure Project

**Framework Preset:**
- Vercel should auto-detect **"Vite"** ✅

**Root Directory:**
- Click **"Edit"** next to Root Directory
- Select `frontend` folder ⚠️ **IMPORTANT**
- Click **"Continue"**

**Build Settings:**
- Build Command: `npm run build` (auto-filled)
- Output Directory: `dist` (auto-filled)
- Install Command: `npm install` (auto-filled)

### 4.4 Add Environment Variables

1. Expand **"Environment Variables"** section
2. Add variable:
   - **Key**: `VITE_API_URL`
   - **Value**: Your Render backend URL (from Step 3.6)
     ```
     https://hrms-lite-backend.onrender.com
     ```
   - ⚠️ **NO trailing slash!**

### 4.5 Deploy

1. Click **"Deploy"**
2. Wait for deployment (takes 1-2 minutes)
3. Watch the build logs

### 4.6 Get Frontend URL

1. Once deployed, you'll see **"Congratulations!"** 🎉
2. Click **"Visit"** or copy the URL (looks like):
   ```
   https://hrms-lite-abc123.vercel.app
   ```
3. **Save this URL** - this is your live application!

### 4.7 Test Live Application

1. Open your Vercel URL in browser
2. You should see the HRMS Lite interface
3. Test adding an employee
4. Test marking attendance
5. Verify everything works!

✅ **Frontend Deployed Successfully!**

---

## Step 5: Update README with Live URLs ⏱️ 2 minutes

### 5.1 Update README.md

Open `README.md` in your project and update the Live Demo section:

```markdown
## 🚀 Live Demo

- **Frontend**: https://hrms-lite-abc123.vercel.app
- **Backend API**: https://hrms-lite-backend.onrender.com
- **API Documentation**: https://hrms-lite-backend.onrender.com/docs
- **GitHub Repository**: https://github.com/YOUR_USERNAME/hrms-lite
```

### 5.2 Commit and Push

```bash
git add README.md
git commit -m "Update README with live deployment URLs"
git push origin main
```

✅ **README Updated!**

---

## Step 6: Final Verification ⏱️ 3 minutes

### 6.1 Test Complete Flow

1. **Open Frontend URL** in browser
2. **Add a test employee:**
   - Employee ID: `EMP001`
   - Name: `John Doe`
   - Email: `john@example.com`
   - Department: `Engineering`
3. **Verify employee appears** in the table
4. **Switch to Attendance tab**
5. **Mark attendance** for the employee
6. **Verify attendance record** appears
7. **Test filter** by selecting the employee from dropdown

### 6.2 Check All Links

- [ ] Frontend loads without errors
- [ ] Backend API is accessible
- [ ] API documentation page works (`/docs`)
- [ ] GitHub repository is public
- [ ] README has all live URLs

### 6.3 Test Error Handling

1. Try adding duplicate employee ID → Should show error
2. Try adding duplicate email → Should show error
3. Try marking attendance twice for same date → Should show error
4. Delete an employee → Should work with confirmation

✅ **All Tests Passed!**

---

## 📝 Submission Checklist

Before submitting your assignment, verify:

- [ ] ✅ Live frontend URL is working
- [ ] ✅ Live backend API is working
- [ ] ✅ GitHub repository is **PUBLIC**
- [ ] ✅ README.md contains all live URLs
- [ ] ✅ Application has no errors on first load
- [ ] ✅ All CRUD operations work
- [ ] ✅ Attendance system works
- [ ] ✅ Error handling works properly

---

## 🎯 URLs to Submit

Copy these and submit with your assignment:

```
Live Frontend: https://[your-app].vercel.app
Live Backend: https://[your-backend].onrender.com
GitHub Repo: https://github.com/[username]/hrms-lite
```

---

## 🔧 Troubleshooting

### Backend Issues

**Problem**: Backend shows "Application failed to respond"
- **Solution**: Check Render logs, verify MongoDB connection string is correct

**Problem**: CORS errors in frontend
- **Solution**: Verify backend CORS is set to allow all origins (`allow_origins=["*"]`)

**Problem**: MongoDB connection timeout
- **Solution**: Check Network Access in MongoDB Atlas, ensure `0.0.0.0/0` is whitelisted

### Frontend Issues

**Problem**: API calls failing
- **Solution**: Verify `VITE_API_URL` environment variable is set correctly in Vercel

**Problem**: Blank page on Vercel
- **Solution**: Check Vercel build logs, ensure root directory is set to `frontend`

**Problem**: Environment variable not working
- **Solution**: Redeploy after adding env vars (Vercel → Deployments → Redeploy)

### Free Tier Limitations

**Render Free Tier:**
- Backend may sleep after 15 minutes of inactivity
- First request after sleep takes 30-60 seconds to wake up
- This is normal for free tier!

**MongoDB Atlas Free Tier:**
- 512 MB storage (more than enough for this project)
- Shared cluster (may have slight latency)

---

## 🎉 Congratulations!

Your HRMS Lite application is now **LIVE** and ready for submission!

**What you've accomplished:**
- ✅ Built a full-stack application
- ✅ Deployed backend to Render
- ✅ Deployed frontend to Vercel
- ✅ Connected to MongoDB Atlas
- ✅ Made it publicly accessible
- ✅ Created professional documentation

---

## 📞 Need Help?

If you encounter issues:
1. Check the troubleshooting section above
2. Review deployment logs in Render/Vercel
3. Verify all environment variables are correct
4. Test backend API directly using `/docs` endpoint

---

**Good Luck with your submission! 🚀**
