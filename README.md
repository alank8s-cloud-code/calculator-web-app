# Python Calculator — Flask + Docker

A web-based calculator application built with **Python and Flask**, designed to run both locally and inside a **Docker container**.

The application provides a browser-based UI for basic arithmetic operations and runs on **port 5000**.

---

# Project Overview

This project demonstrates the complete journey of a Python web application:

```text
Python Application
       ↓
Flask Web Framework
       ↓
HTML + CSS UI
       ↓
Run Locally
       ↓
Dockerfile
       ↓
Docker Image
       ↓
Docker Container
       ↓
Browser
```

---

# What, Why, How?

## What?

This is a Flask-based calculator application that allows users to perform:

* Addition
* Subtraction
* Multiplication
* Division

It includes input validation and division-by-zero handling.

The application can run:

1. Directly with Python
2. Inside a Docker container

---

## Why?

This project helps understand the complete lifecycle of a Python application before moving into production-style DevOps workflows.

You learn:

* Python application structure
* Flask
* HTTP requests
* HTML forms
* CSS
* Flask templates
* Static files
* Python dependencies
* Virtual environments
* Docker images
* Docker containers
* Port mapping

---

## How?

The application is developed and tested locally first:

```text
Python
  ↓
Flask
  ↓
localhost:5000
```

After confirming that it works, it is packaged into a Docker image:

```text
Python Application
       ↓
   Dockerfile
       ↓
   Docker Image
       ↓
Docker Container
       ↓
localhost:5000
```

---

# Project Structure

```text
python-calculator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── Dockerfile
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

# Application Architecture

```text
                         Browser
                            │
                            │ HTTP
                            ▼
                   http://localhost:5000
                            │
                            ▼
                    ┌──────────────┐
                    │    Flask     │
                    │    app.py    │
                    └──────┬───────┘
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
      Calculator Logic          render_template()
              │                         │
              │                         ▼
              │                templates/index.html
              │                         │
              │                         ▼
              │                  static/style.css
              │                         │
              └────────────┬────────────┘
                           ▼
                         Result
```

---

# Application Components

## `app.py`

### What?

The main Python application.

### Why?

It contains:

* Flask configuration
* Routes
* Calculator logic
* Form handling
* Error handling
* Port configuration

### How?

The Flask application is created with:

```python
app = Flask(__name__)
```

The application runs on port `5000`:

```python
app.run(host="0.0.0.0", port=5000, debug=True)
```

---

# `templates/index.html`

### What?

The calculator's HTML interface.

### Why?

It provides the UI where users enter numbers and select operations.

### How?

Flask renders it using:

```python
render_template("index.html")
```

Flask automatically searches for templates inside:

```text
templates/
```

---

# `static/style.css`

### What?

The CSS file that controls the appearance of the calculator.

### Why?

HTML provides structure while CSS provides styling.

### How?

The HTML connects to CSS using:

```html
<link
    rel="stylesheet"
    href="{{ url_for('static', filename='style.css') }}"
>
```

Flask serves:

```text
/static/style.css
```

from:

```text
static/style.css
```

---

# `requirements.txt`

### What?

A list of Python dependencies required by the application.

### Why?

It allows the same dependencies to be installed consistently on another machine or inside Docker.

### How?

Install dependencies with:

```bash
pip install -r requirements.txt
```

For this project, Flask is the main external dependency.

Check the installed Flask version:

```bash
python -m flask --version
```

You can regenerate the requirements file with:

```bash
python -m pip freeze > requirements.txt
```

---

# `.gitignore`

The `.gitignore` prevents unnecessary or sensitive files from being committed.

Example:

```gitignore
.venv/
venv/
env/

__pycache__/
*.py[cod]

.env
.env.*

.vscode/
.idea/

*.log

.DS_Store
Thumbs.db
```

---

# Flask Request Flow

When the user opens:

```text
http://localhost:5000
```

the browser sends:

```text
GET /
```

Flask receives the request:

```text
GET /
  ↓
@app.route("/")
  ↓
index()
  ↓
render_template()
  ↓
index.html
```

The browser then displays the calculator.

---

# Calculator Request Flow

When the user submits:

```text
First Number: 10
Second Number: 5
Operation: Addition
```

the browser sends:

```text
POST /
```

with:

```text
num1=10
num2=5
operation=add
```

Flask receives the values:

```python
num1 = float(request.form["num1"])
num2 = float(request.form["num2"])
operation = request.form["operation"]
```

Then:

```text
request.form
     ↓
calculate()
     ↓
result
     ↓
index.html
     ↓
Browser
```

---

# Error Handling

## Division by Zero

The application checks:

```python
if num2 == 0:
    raise ValueError("Cannot divide by zero.")
```

Therefore:

```text
10 ÷ 0
```

does not crash the application.

Instead, the user receives:

```text
Error
Cannot divide by zero.
```

---

# Local Python Setup

Before Dockerizing the application, make sure it works directly with Python.

## Step 1 — Create virtual environment

```bash
python3 -m venv .venv
```

---

## Step 2 — Activate virtual environment

### Linux/macOS

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

## Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4 — Check Flask

```bash
python -m flask --version
```

---

## Step 5 — Run the application

```bash
python app.py
```

The application should run on:

```text
http://localhost:5000
```

---

# Test the Local Application

Open:

```text
http://localhost:5000
```

Test:

```text
10 + 5
10 - 5
10 × 5
10 ÷ 5
10 ÷ 0
```

Also test invalid input.

The application should continue running when invalid input is provided.

---

# Dockerization

Once the application works correctly with Python, we can package it using Docker.

The Docker workflow is:

```text
              Python Source Code
                      │
                      ▼
                 Dockerfile
                      │
                      ▼
                docker build
                      │
                      ▼
                Docker Image
                      │
                      ▼
                 docker run
                      │
                      ▼
              Docker Container
                      │
                      ▼
                Flask :5000
                      │
                      ▼
            http://localhost:5000
```

---

# Dockerfile

Create a file named:

```text
Dockerfile
```

Example:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

---

# Dockerfile — What, Why, How?

## `FROM`

```dockerfile
FROM python:3.12-slim
```

### What?

Selects the base image.

### Why?

Our application needs Python.

### How?

Docker starts from a Python 3.12 slim image.

---

## `WORKDIR`

```dockerfile
WORKDIR /app
```

### What?

Sets the working directory inside the container.

### Why?

It gives the application a predictable location.

Inside the container:

```text
/app
```

becomes the project directory.

---

## `COPY requirements.txt`

```dockerfile
COPY requirements.txt .
```

### What?

Copies the dependency file into the image.

### Why?

We need the dependencies before running the application.

---

## `RUN pip install`

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

### What?

Installs Python dependencies.

### Why?

The container needs Flask to run the application.

---

## `COPY . .`

```dockerfile
COPY . .
```

### What?

Copies the project files into the container.

### Why?

The container needs:

```text
app.py
templates/
static/
```

---

## `EXPOSE`

```dockerfile
EXPOSE 5000
```

### What?

Documents that the application listens on port `5000`.

### Why?

It communicates the intended application port.

> `EXPOSE` alone does **not** publish the port to your host machine.

---

## `CMD`

```dockerfile
CMD ["python", "app.py"]
```

### What?

Defines the default command executed when the container starts.

### Why?

It starts the Flask application.

---

# Build the Docker Image

From the project directory:

```bash
docker build -t python-calculator .
```

### What happens?

```text
Dockerfile
    ↓
docker build
    ↓
Base Python Image
    ↓
Install Flask
    ↓
Copy Application
    ↓
Python Calculator Image
```

Check the image:

```bash
docker images
```

You should see:

```text
python-calculator
```

---

# Run the Docker Container

Run:

```bash
docker run -d -p 5000:5000 --name python-calculator python-calculator
```

Now open:

```text
http://localhost:5000
```

---

# Understanding `-p 5000:5000`

This is one of the most important Docker concepts.

```bash
-p 5000:5000
```

means:

```text
HOST PORT : CONTAINER PORT
```

Therefore:

```text
5000 : 5000
```

means:

```text
Your Computer
localhost:5000
      │
      │ Docker port mapping
      ▼
Container
port 5000
      │
      ▼
Flask
```

So when you visit:

```text
http://localhost:5000
```

the request reaches Flask inside the container.

---

# Why `host="0.0.0.0"` Matters

Our Flask application uses:

```python
app.run(host="0.0.0.0", port=5000)
```

This is especially important inside Docker.

If Flask only listens on:

```text
127.0.0.1
```

inside the container, external traffic may not be able to reach it correctly.

Using:

```text
0.0.0.0
```

allows Flask to listen on the container's network interfaces.

The complete connection becomes:

```text
Browser
   │
   │ localhost:5000
   ▼
Host Machine :5000
   │
   │ -p 5000:5000
   ▼
Container :5000
   │
   ▼
Flask 0.0.0.0:5000
   │
   ▼
Python Application
```

---

# Check Running Containers

```bash
docker ps
```

You should see:

```text
python-calculator
```

---

# View Container Logs

```bash
docker logs python-calculator
```

This is useful for checking whether Flask started successfully.

You should see something similar to:

```text
* Running on http://127.0.0.1:5000
* Running on http://172.x.x.x:5000
```

---

# Stop the Container

```bash
docker stop python-calculator
```

---

# Start the Existing Container Again

```bash
docker start python-calculator
```

---

# Remove the Container

Stop it first:

```bash
docker stop python-calculator
```

Then:

```bash
docker rm python-calculator
```

---

# Run Container in Foreground

For development and debugging, you can run:

```bash
docker run --rm -p 5000:5000 --name python-calculator python-calculator
```

The logs will appear directly in your terminal.

Press:

```text
Ctrl + C
```

to stop it.

---

# Run Container in Background

For normal usage:

```bash
docker run -d \
    -p 5000:5000 \
    --name python-calculator \
    python-calculator
```

Check:

```bash
docker ps
```

Then visit:

```text
http://localhost:5000
```

---

# Docker Commands Cheat Sheet

## Build

```bash
docker build -t python-calculator .
```

## Run

```bash
docker run -d -p 5000:5000 --name python-calculator python-calculator
```

## List images

```bash
docker images
```

## List running containers

```bash
docker ps
```

## List all containers

```bash
docker ps -a
```

## View logs

```bash
docker logs python-calculator
```

## Stop

```bash
docker stop python-calculator
```

## Start

```bash
docker start python-calculator
```

## Remove container

```bash
docker rm python-calculator
```

## Remove image

```bash
docker rmi python-calculator
```

---

# Complete Development Workflow

The recommended workflow is:

```text
┌──────────────────────┐
│ 1. Write Python Code │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 2. Build Flask UI    │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 3. Test Locally      │
│ python app.py        │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 4. Create Dockerfile │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 5. Build Image       │
│ docker build         │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 6. Run Container     │
│ docker run           │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 7. Test Browser      │
│ localhost:5000       │
└──────────────────────┘
```

---

# Final Architecture

After Dockerization:

```text
                         HOST MACHINE
                              │
                              │
                    localhost:5000
                              │
                              ▼
                    ┌─────────────────┐
                    │     Docker      │
                    │    Container    │
                    │                 │
                    │  Flask :5000    │
                    │       │         │
                    │       ▼         │
                    │    app.py       │
                    │       │         │
                    │       ├── templates/
                    │       │     └── index.html
                    │       │
                    │       └── static/
                    │             └── style.css
                    │                 │
                    └─────────────────┘
                              │
                              ▼
                           Browser
```

---

# Final Checklist

Before considering the project complete:

* [ ] Python application works
* [ ] Flask installed
* [ ] `requirements.txt` created
* [ ] HTML UI works
* [ ] CSS loads correctly
* [ ] Calculator operations work
* [ ] Division by zero is handled
* [ ] `.gitignore` exists
* [ ] `README.md` exists
* [ ] Dockerfile exists
* [ ] Docker image builds successfully
* [ ] Docker container starts successfully
* [ ] Port `5000` is mapped
* [ ] Application works at `http://localhost:5000`
* [ ] Container logs show Flask running

---

# Key DevOps Lesson

The application has two different environments:

### Local Python

```text
Your Machine
    ↓
Python
    ↓
Flask
    ↓
localhost:5000
```

### Docker

```text
Your Machine
    ↓
Docker
    ↓
Container
    ↓
Python
    ↓
Flask
    ↓
localhost:5000
```

The **application code remains the same**.

Docker provides a consistent environment in which that application runs.

