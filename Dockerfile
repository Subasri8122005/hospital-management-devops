# ---------------------------------------------------------
# Hospital Management System
# Dockerfile
# ---------------------------------------------------------

FROM python:3.12-slim

# Prevent Python from creating .pyc files
# and enable unbuffered application logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set application working directory
WORKDIR /app

# Install Python dependencies first
# This improves Docker build cache efficiency
COPY app/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app/ .

# Application port
EXPOSE 5000

# Start Flask application
CMD ["python", "app.py"]
