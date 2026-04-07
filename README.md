# 🚀 Job Tracker API

A production-ready **Job Application Tracker API** built using FastAPI. This project helps users manage and track their job applications efficiently with secure authentication and RESTful APIs.

---

## 📌 Features

* 🔐 User Authentication (JWT-based login & register)
* 📄 Add & manage job applications
* 📊 Track application status (Applied, Interview, Rejected, Offer)
* 🔍 Search and filter jobs
* 📑 Pagination support
* 🛡️ Secure API endpoints
* ⚡ Fast performance with FastAPI

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Database:** SQLite (can be upgraded to PostgreSQL)
* **ORM:** SQLAlchemy
* **Authentication:** JWT (python-jose)
* **Password Hashing:** Passlib
* **Server:** Uvicorn

---

## 📂 Project Structure

```
job-tracker/
│── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── routes/
│   │    ├── user.py
│   │    ├── jobs.py
│
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/Niranjan1014/job-tracker-api.git
cd job-tracker-api
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run the server

```
uvicorn app.main:app --reload
```

---

## 🌐 API Documentation

After running the server, open:

👉 http://127.0.0.1:8000/docs

Interactive Swagger UI will appear.

---

## 🔑 API Endpoints

### Auth

* `POST /register` → Register new user
* `POST /login` → Login & get token

### Jobs

* `POST /jobs` → Create job
* `GET /jobs` → Get all jobs

---

## 🚀 Future Improvements

* ✅ Role-based authentication
* ✅ Email notifications
* ✅ Frontend integration (React)
* ✅ Deployment (Render / Railway)
* ✅ Docker support

---

## 💡 What I Learned

* Building scalable APIs with FastAPI
* Implementing JWT authentication
* Database design with SQLAlchemy
* Writing clean and maintainable backend code

---

