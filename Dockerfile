FROM python:3.11-slim
LABEL maintainer="woocat.python.com"


WORKDIR /app
COPY requirements.txt ./
COPY src ./src
COPY .env ./
RUN pip install --no-cache-dir -r requirements.txt
