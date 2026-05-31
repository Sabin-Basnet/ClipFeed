# ClipFeed 📸

A modern photo and video sharing platform built with **FastAPI** backend and **Streamlit** frontend. Share your media, caption them, and view a social feed in real-time.

## 🎯 Project Overview

ClipFeed is a full-stack social media application that allows users to:
- **Register and authenticate** with JWT-based authentication
- **Upload images and videos** with automatic cloud storage via ImageKit
- **Add captions** to their media posts
- **View a live feed** of all posts from the community
- **Delete their own posts**V anytime

## 🏗️ Project Architecture

### Backend (FastAPI)
Located in the `app/` directory, the backend handles:

```
app/
├── app.py          # Main FastAPI application with routes
├── db.py           # Database models (User, Post) and SQLite setup
├── users.py        # Authentication logic with JWT and fastapi-users
├── images.py       # ImageKit SDK configuration for media uploads
└── schemas.py      # Pydantic schemas for API request/response validation

```

**Key Features:**
- **Authentication**: JWT-based user authentication with password hashing
- **Database**: SQLite with async SQLAlchemy ORM
- **File Storage**: ImageKit cloud storage for media files
- **API Routes**:
  - `POST /auth/jwt/login` - User login
  - `POST /auth/register` - User registration
  - `POST /upload` - Upload image/video (requires auth)
  - `GET /feed` - Get all posts (requires auth)
  - `DELETE /posts/{post_id}` - Delete a post (requires auth)
  - `/users/*` - User management routes

### Frontend (Streamlit) #Just Basic
Located in `frontend.py`, the web interface provides:
- **Login/Sign-up page** - User authentication UI
- **Upload page** - Media upload with caption input
- **Feed page** - View community posts with delete functionality
- **Session management** - Maintains JWT tokens for authenticated requests

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | FastAPI, SQLAlchemy (async), SQLite |
| **Frontend** | Streamlit |
| **Authentication** | fastapi-users, JWT |
| **File Storage** | ImageKit SDK |
| **Database** | SQLite with aiosqlite |
| **Server** | Uvicorn |

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- ImageKit Account (for media storage)

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone "https://github.com/Sabin-Basnet/ClipFeed.git"
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory with your ImageKit credentials:

```env
IMAGEKIT_PRIVATE_KEY=your_imagekit_private_key
IMAGEKIT_PUBLIC_KEY=your_imagekit_public_key
IMAGEKIT_URL=https://ik.imagekit.io/your_imagekit_id
JWT_SECRET=your_secret_key_for_jwt
```

**How to get ImageKit credentials:**
1. Sign up at [ImageKit.io](https://imagekit.io)
2. Go to Settings → Developer Options
3. Copy your Private Key (for server uploads)
4. Note your URL Endpoint for the IMAGEKIT_URL

### 5. Run the Application

#### Option A: Run Backend and Frontend Separately

**Terminal 1 - Start Backend (FastAPI Server):**
```bash
python main.py
```
The API server will start at `http://localhost:8000`

**Terminal 2 - Start Frontend (Streamlit App):**
```bash
streamlit run frontend.py
```
The web interface will open at `http://localhost:8501`

#### Option B: Run Both Concurrently

```bash
# Terminal 1
python main.py

# Terminal 2 (in a new terminal)
streamlit run frontend.py
```

## 🚀 How to Use the Application

### 1. **Register a New Account**
   - Go to the Streamlit frontend
   - Enter your email and password
   - Click "Sign Up"
   - Account is created and ready to use

### 2. **Login**
   - Enter your registered email and password
   - Click "Login"
   - You'll be authenticated and taken to the main app

### 3. **Upload Media**
   - Click "📸 Upload" in the sidebar
   - Select an image or video file
   - Add a caption (optional)
   - Click "Share"
   - Your post will appear in the feed

### 4. **View Feed**
   - Click "🏠 Feed" in the sidebar
   - See all posts from all users
   - Posts show the user's email, creation date, and media

### 5. **Delete Your Posts**
   - In the feed, find your own posts
   - Click the "🗑️" button on your posts
   - Post will be permanently deleted

### 6. **Logout**
   - Click the "Logout" button in the sidebar


## 📁 Database Schema

### Users Table
- `id` (UUID) - Primary key
- `email` (String) - User email
- `password` (String) - Hashed password
- Other FastAPI-Users fields

### Posts Table
- `id` (UUID) - Primary key
- `user_id` (UUID) - Foreign key to Users
- `caption` (Text) - Post caption
- `url` (String) - ImageKit media URL
- `file_type` (String) - "image" or "video"
- `file_name` (String) - Original filename
- `created_at` (DateTime) - Post creation timestamp

## 🐛 Troubleshooting

### ImageKit Upload Fails
- Verify `IMAGEKIT_PRIVATE_KEY` is correct in `.env`
- Check that your ImageKit account is active
- Ensure file size is within ImageKit limits
- Max size -> 100 MB 

### Authentication Fails
- Make sure `JWT_SECRET` is set in `.env`
- Clear browser cookies/cache and try login again
- Use a fresh password reset if needed

### Frontend Can't Connect to Backend
- Ensure backend is running on `http://localhost:8000`
- Check that port 8000 is not in use

## 📦 Project Dependencies

```
fastapi          - Web framework
uvicorn          - ASGI server
sqlalchemy       - ORM
aiosqlite        - Async SQLite driver
fastapi-users    - Authentication system
pydantic         - Data validation
imagekitio       - Media storage SDK
streamlit        - Frontend framework
python-dotenv    - Environment variable management
requests         - HTTP client for frontend
```

**Thank You** 
