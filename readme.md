# Assing Project

**Assing** is a full-stack web application with [Flask](https://flask.palletsprojects.com/) backend for data-centric operations and an [Express.js](https://expressjs.com/) frontend for dynamic routing and UI management.

## 🚀 Architecture Overview
- **Backend:** Python/Flask (Port 8000) - Handles API logic and database interactions.
- **Frontend:** Node.js/Express (Port 3000) - Serves the user interface and proxies specific requests to the backend.

## 🔧 Installation & Setup

### 1. Backend (Flask)
Navigate to the backend directory and set up a virtual environment:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Run the Flask server:
```bash
python app.py
```

### 2. Frontend (Express.js)
In a new terminal window, navigate to the frontend directory and install dependencies:
```bash
cd frontend
npm install
```

Run the Express server:
```bash
npm start
```
