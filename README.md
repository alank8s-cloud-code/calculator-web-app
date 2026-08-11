# Python Calculator — Flask Web Application

A simple web-based calculator built with **Python and Flask**.

The application provides a browser-based UI for performing basic arithmetic operations and runs on **port 5000**.

---

## Project Overview

This project demonstrates how a Python application can be converted from a command-line program into a web application.

The application uses:

* **Python** — Application logic
* **Flask** — Web framework
* **HTML** — Web page structure
* **CSS** — Web page styling
* **Jinja2** — Dynamic HTML rendering
* **Virtual Environment** — Dependency isolation

---

# Project Architecture

```text
Browser
   │
   │ http://localhost:5000
   ▼
┌─────────────────────┐
│       Flask         │
│       app.py        │
└──────────┬──────────┘
           │
           ├──────────────► Calculator Logic
           │
           ▼
┌─────────────────────┐
│ templates/index.html│
│       HTML UI       │
└──────────┬──────────┘
           │
           │ loads
           ▼
┌─────────────────────┐
│ static/style.css    │
│       CSS           │
└─────────────────────┘
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
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

# What, Why, How?

## 1. `app.py`

### What?

`app.py` is the main Python application.

### Why?

It contains the Flask server, routes, request handling, calculator logic, and error handling.

### How?

Flask is initialized with:

```python
app = Flask(__name__)
```

The application is started on port 5000:

```python
app.run(host="0.0.0.0", port=5000, debug=True)
```

---

## 2. `templates/index.html`

### What?

`index.html` is the calculator's web interface.

### Why?

Users need a browser-based interface to enter numbers and select operations.

### How?

Flask renders the HTML using:

```python
render_template("index.html")
```

Flask automatically looks for HTML templates inside the `templates/` directory.

---

## 3. `static/style.css`

### What?

`style.css` contains the application's visual styling.

### Why?

HTML provides the structure, while CSS controls the appearance.

### How?

The HTML connects to the CSS using:

```html
<link
    rel="stylesheet"
    href="{{ url_for('static', filename='style.css') }}"
>
```

Flask serves the CSS from:

```text
static/style.css
```

The browser then applies the CSS to the HTML.

---

# How HTML Connects to CSS

The connection works like this:

```text
Browser requests /
       │
       ▼
Flask
       │
       ▼
templates/index.html
       │
       │ Browser sees:
       │ /static/style.css
       ▼
Browser requests CSS
       │
       ▼
Flask serves
static/style.css
       │
       ▼
Browser combines
HTML + CSS
       │
       ▼
Styled Calculator
```

---

# Features

The calculator supports:

* Addition
* Subtraction
* Multiplication
* Division
* Decimal numbers
* Input validation
* Division-by-zero handling
* Invalid operation handling
* Browser-based UI
* Responsive layout
* Flask web server

---

# Calculator Operations

| Operation      | Symbol | Example  | Result |
| -------------- | ------ | -------- | -----: |
| Addition       | `+`    | `10 + 5` |   `15` |
| Subtraction    | `-`    | `10 - 5` |    `5` |
| Multiplication | `×`    | `10 × 5` |   `50` |
| Division       | `÷`    | `10 ÷ 5` |    `2` |

---

# Error Handling

## Division by Zero

The application checks for division by zero:

```python
if num2 == 0:
    raise ValueError("Cannot divide by zero.")
```

Instead of crashing, the application displays an error message.

Example:

```text
Error
Cannot divide by zero.
```

---

## Invalid Input

The application converts user input into numbers:

```python
num1 = float(request.form["num1"])
```

Invalid values are caught and handled using:

```python
try:
    ...
except ValueError:
    ...
```

This prevents invalid user input from crashing the application.

---

# Requirements

The project requires:

* Python 3
* Flask

Dependencies are stored in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

---

# Local Setup

## Step 1 — Clone the repository

```bash
git clone <your-repository-url>
cd python-calculator
```

---

## Step 2 — Create a virtual environment

```bash
python3 -m venv .venv
```

---

## Step 3 — Activate the virtual environment

### Linux/macOS

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

## Step 4 — Install dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5 — Run the application

```bash
python app.py
```

The Flask server will start on:

```text
http://localhost:5000
```

---

# Access the Application

Open your browser and visit:

```text
http://localhost:5000
```

You should see the Python Calculator UI.

---

# Application Request Flow

When the user opens the application:

```text
Browser
   │
   │ GET /
   ▼
Flask
   │
   ▼
index()
   │
   ▼
render_template()
   │
   ▼
index.html
   │
   ▼
Browser
```

When the user submits a calculation:

```text
Browser
   │
   │ POST /
   │
   │ num1
   │ num2
   │ operation
   ▼
Flask
   │
   ▼
request.form
   │
   ▼
calculate()
   │
   ▼
Result
   │
   ▼
index.html
   │
   ▼
Browser
```

---

# CSS Request Flow

The browser receives:

```html
<link
    rel="stylesheet"
    href="{{ url_for('static', filename='style.css') }}"
>
```

Flask generates the static file URL:

```text
/static/style.css
```

The browser requests it:

```text
GET /static/style.css
```

Flask serves:

```text
static/style.css
```

The browser applies the CSS to the HTML.

---

# Useful Commands

### Check Python version

```bash
python3 --version
```

### Create virtual environment

```bash
python3 -m venv .venv
```

### Activate virtual environment

```bash
source .venv/bin/activate
```

### Install Flask

```bash
pip install flask
```

### Generate requirements

```bash
pip freeze > requirements.txt
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Run application

```bash
python app.py
```

### Check Git status

```bash
git status
```

---

# Git Workflow

Initialize Git:

```bash
git init
```

Add files:

```bash
git add .
```

Create the first commit:

```bash
git commit -m "Build Flask calculator application"
```

Connect your GitHub repository:

```bash
git remote add origin <your-repository-url>
```

Push:

```bash
git branch -M main
git push -u origin main
```

---

# Learning Outcomes

After completing this project, you should understand:

* How a Python application runs
* How Flask works
* How routes work
* Difference between GET and POST
* How HTML forms send data to Flask
* How `request.form` works
* How Python processes user input
* How calculator logic is separated from request handling
* How errors are handled
* How Flask serves HTML
* How Flask serves CSS
* How `templates/` works
* How `static/` works
* How a browser communicates with a Python backend
* How to run a Flask application on port 5000
* How Python dependencies are managed with `requirements.txt`
* How Git tracks the project

---

# Next Step — Dockerization

After confirming that the application works locally:

```bash
python app.py
```

and is accessible at:

```text
http://localhost:5000
```

the next DevOps step is to containerize it.

The Docker workflow will be:

```text
Python Application
       │
       ▼
requirements.txt
       │
       ▼
Dockerfile
       │
       ▼
Docker Image
       │
       ▼
Docker Container
       │
       ▼
Flask :5000
       │
       ▼
Browser
```

> **Important:** Dockerization should come after the application works correctly in the native Python environment.

