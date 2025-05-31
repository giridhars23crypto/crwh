# Use the official Python image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY webhook.py .

# Run the application
CMD exec gunicorn --bind :8080 webhook:app
