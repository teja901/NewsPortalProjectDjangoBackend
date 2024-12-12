# Use official Python image as a base image
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install Redis
RUN apt-get update && apt-get install -y redis-server

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]