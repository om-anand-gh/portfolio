# --- Build stage ---
FROM python:3.13-slim AS builder

# Install dependencies for building Python packages
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy and install Python dependencies
COPY requirements/base.txt .
RUN pip install --no-compile --no-cache-dir -r base.txt


# --- Runtime stage ---
FROM python:3.13-slim

# Install only runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY . /app/

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    SECRET_KEY=secret

# Collect static files
RUN python manage.py collectstatic --noinput

# Start app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "server.wsgi"]
