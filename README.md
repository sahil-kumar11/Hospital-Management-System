# 🏥 Hospital Management System

A web-based **Hospital Management System** developed using **Django** that helps administrators efficiently manage doctors, patients, and appointments through a secure dashboard.

This project demonstrates the practical implementation of Django's authentication system, database relationships, CRUD operations, and template rendering.

---

## 📌 Project Overview

The Hospital Management System is designed to simplify hospital administrative tasks by providing a centralized platform for managing essential hospital records.

The system allows administrators to:

- Manage doctor records
- Manage patient information
- Schedule appointments
- View hospital statistics through a dashboard
- Securely access the system using an authenticated admin account

---

## ✨ Features

### 🔐 Authentication System
- Admin login functionality
- Session-based authentication using Django
- Restricted access to authorized staff members only
- Secure logout mechanism

### 👨‍⚕️ Doctor Management
- Add new doctors
- View all registered doctors
- Delete doctor records
- Store doctor's specialization and contact information

### 🧑‍🤝‍🧑 Patient Management
- Add patient details
- View patient records
- Delete patient information
- Store patient contact details and address

### 📅 Appointment Management
- Schedule appointments between doctors and patients
- Select doctors and patients dynamically
- View appointment schedules
- Delete appointments when required

### 📊 Admin Dashboard
Displays real-time statistics including:

- Total Doctors
- Total Patients
- Total Appointments

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend Programming |
| Django | Web Framework |
| SQLite | Database |
| HTML5 | Structure |
| CSS3 | Styling |
| Bootstrap | Responsive UI |
| Django Templates | Dynamic Frontend Rendering |

---

## 🗂️ Database Models

### Doctor Model

Stores doctor information.

```python
Doctor
├── name
├── mobile
└── special
```

### Patient Model

Stores patient details.

```python
Patient
├── name
├── gender
├── mobile
└── address
```

### Appointment Model

Maintains relationships between doctors and patients.

```python
Appointment
├── doctor (Foreign Key)
├── patient (Foreign Key)
├── date
└── time
```

---

## 📁 Project Structure

```text
HospitalMangmt/
│
├── manage.py
├── db.sqlite3
│
├── HospitalMangmt/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── hospital/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── migrations/
│   ├── static/
│   └── templates/
│
└── ...
```

---

## 🚀 Installation Guide

### Clone the Repository

```bash
git clone https://github.com/your-username/Hospital-Management-System.git
```

### Move to Project Directory

```bash
cd Hospital-Management-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Development Server

```bash
python manage.py runserver
```

Open the browser and visit:

```
http://127.0.0.1:8000/
```

---

## 🔑 Admin Access

Create an administrator account using:

```bash
python manage.py createsuperuser
```

Use the credentials to log into the system.

---

## 📚 Learning Outcomes

Through this project, the following concepts were practiced:

- Django Project Structure
- Django Authentication System
- CRUD Operations
- Model Relationships using Foreign Keys
- Django Templates
- Static File Management
- URL Routing
- Database Integration with SQLite
- Session Management

---

## 🎯 Future Improvements

Possible enhancements include:

- Edit functionality for doctors and patients
- Search and filtering options
- Email notifications for appointments
- Patient medical history management
- Doctor availability scheduling
- Role-based authentication
- REST API integration
- Deployment on cloud platforms

---

## 📷 Screens Included

The application consists of the following interfaces:

- Login Page
- Dashboard
- Add Doctor Page
- View Doctors Page
- Add Patient Page
- View Patients Page
- Add Appointment Page
- View Appointments Page
- About Page
- Contact Page

---

## 👨‍💻 Author

**Developed by:** *Sahil Kumar*

This project was built as part of my learning journey in **Django Web Development** to strengthen my understanding of backend development and database-driven applications.

---

## 📄 License

This project is developed for **educational and portfolio purposes**.

Feel free to fork, modify, and enhance it for learning purposes.
