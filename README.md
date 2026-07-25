# Employee Management App

A simple Employee Management web application built with Flask and containerized using Docker.

## Features

- View employee list
- Add new employees
- Lightweight Flask application
- Dockerized for easy deployment

## Tech Stack

- Python 3
- Flask
- Docker

## Project Structure

```text
employee-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## Run Locally

### Clone the Repository

```bash
git clone https://github.com/Krishna9451/employee-app
cd employee-app
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

## Docker Setup

### Build Docker Image

```bash
docker build -t employee-app .
```

### Run Docker Container

```bash
docker run -d -p 5000:5000 --name employee-container employee-app
```

Open:

```text
http://localhost:5000
```

## Learning Objectives

This project was created to practice:

- Flask Web Development
- Git & GitHub
- Docker Containerization
- Linux Commands
- DevOps Fundamentals

## Author

Shri Krishna Yadav

B.Tech CSE, JSS Academy of Technical Education, Noida
