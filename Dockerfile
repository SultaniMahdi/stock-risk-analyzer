FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy both src folder and app.py
COPY src/ ./src
COPY app.py ./app.py

EXPOSE 5000

CMD ["python", "app.py"]

