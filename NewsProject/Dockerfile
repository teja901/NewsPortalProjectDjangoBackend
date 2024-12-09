# Use official Python image as a base image
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "NewsProject.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--reload"]
