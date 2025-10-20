# Dockerfile
FROM python:3.11-slim

# set a user for better security
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# copy only what's needed for deps first to leverage cache
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY . .

# create a non-root user and switch to it (optional but recommended)
RUN useradd --create-home --shell /bin/bash appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 5000
CMD ["python", "app.py"]
