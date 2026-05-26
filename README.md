# 🚀 Flask CI/CD Pipeline Project

A production-style Flask application with complete CI/CD pipeline using **GitHub Actions + Docker + Docker Hub**.

---

# 📌 Project Overview

This project demonstrates a full DevOps workflow:

- Flask REST API
- Automated testing using Pytest
- Docker containerization
- CI/CD using GitHub Actions
- Docker Hub image publishing
- Automated build and deployment pipeline

---

# 🏗️ Architecture

```text
Developer → GitHub → GitHub Actions → Tests → Docker Build → Docker Hub
```

---

# 📂 Project Structure

```text
flask-cicd-app/
│
├── app/
│   ├── __init__.py
│   └── routes.py
│
├── tests/
│   ├── test_routes.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── requirements.txt
├── wsgi.py
└── README.md
```

---

# ⚙️ Features

- Flask API with health check
- Unit testing with Pytest
- Code coverage support
- Dockerized application
- CI/CD pipeline automation
- Docker Hub integration

---

# 🌐 API Endpoints

## Home Endpoint

```http
GET /
```

Response:
```json
{
  "message": "Hello from Flask CI/CD app!",
  "status": "ok"
}
```

---

## Health Endpoint

```http
GET /health
```

Response:
```json
{
  "status": "healthy"
}
```

---

# ▶️ How to Run Project Locally

## 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/flask-cicd-app.git
cd flask-cicd-app
```

---

## 2. Create Virtual Environment

### Windows
```bash
py -m venv venv
venv\Scripts\activate
```

### Linux/Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Application

```bash
python -m flask --app wsgi:app run
```

Open:
```text
http://127.0.0.1:5000
```

---

## 5. Run Tests

```bash
pytest --cov=app
```

---

# 🐳 Docker Setup

## Build Image
```bash
docker build -t flask-cicd-app .
```

## Run Container
```bash
docker run -p 5000:5000 flask-cicd-app
```

---

# 🔄 CI/CD Pipeline

Every push to `main` triggers:

1. Install dependencies
2. Run tests
3. Build Docker image
4. Push image to Docker Hub

---

# 📸 Screenshots Required

## 1️⃣ GitHub Repository
- Project structure
- README view

📌 File:
```text
Screenshots/github-repo.png
```

---

## 2️⃣ GitHub Actions Success
- Workflow passed
- All green checks

📌 File:
```text
Screenshots/github-actions.png
```

---


## 3️⃣ Pytest Output
- Tests passed
- Coverage report

📌 File:
```text
Screenshots/pytest.png
```

---

## 4️⃣ Flask App Running
- Browser output of `/`

📌 File:
```text
Screenshots/flask-home.png
```

---

## 5️⃣ Health Endpoint
- `/health` response

📌 File:
```text
Screenshots/health.png
```

---

## 6️⃣ Docker Hub Image
- Tags (latest + SHA)

📌 File:
```text
Screenshots/dockerhub.png
```

---

# 📂 Screenshot Folder Structure

```text
screenshots/
├── github-repo.png
├── github-actions.png
├── pytest.png
├── flask-home.png
├── health.png
└── dockerhub.png
```

---

# 🧹 Resource Cleanup

## Stop Local Server
```bash
CTRL + C
```

## Remove venv
```bash
rm -rf venv
```

## Remove Docker Containers
```bash
docker stop <container_id>
docker rm <container_id>
```

## Remove Images
```bash
docker rmi <image_id>
```

---

# 💡 Key Learnings

- CI/CD pipeline automation
- Docker containerization
- GitHub Actions workflow
- Flask API development
- DevOps deployment flow

---



