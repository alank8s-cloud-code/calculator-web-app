#Base image of the project

FROM python:3.12-alpine

# Set the working directory

WORKDIR /app

# Copy the dependency

COPY requirements.txt .

# Install the Dependency

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt 

# Copy the all files

COPY . .

# Expose the Port

EXPOSE 5000

# Run the application

CMD ["python", "app.py"]
