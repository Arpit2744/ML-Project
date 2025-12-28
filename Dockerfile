FROM python:3.10-slim

WORKDIR /app

# 1. Install System Dependencies FIRST
RUN apt-get update && apt-get install -y awscli

# 2. Copy Requirements 
COPY requirements.txt .

# 3. Install Python Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy Application Code 
COPY . .

CMD ["python3", "app.py"]