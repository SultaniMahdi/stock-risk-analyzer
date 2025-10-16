# Use a lightweight Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn (production WSGI server)
RUN pip install gunicorn

# Copy your source code
COPY src/ ./src
COPY app.py ./app.py

# Expose Flask/Gunicorn port
EXPOSE 5000

# Run app with Gunicorn instead of Flask dev server
# 'app:app' means "import app.py and use the 'app' Flask instance"
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

