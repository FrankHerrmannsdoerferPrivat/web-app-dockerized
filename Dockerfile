# syntax=docker/dockerfile:1
FROM python:3.13-slim

# Your pyproject requires Python >=3.13,<4.0
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# If you don't need to compile native wheels, you can drop build-essential
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
 && rm -rf /var/lib/apt/lists/*

# Copy project metadata and source
COPY pyproject.toml README.md ./
COPY src ./src

# Install runtime deps
# - First Gunicorn (server)
# - Then your project; pip will read [project] deps from pyproject.toml via poetry-core
RUN pip install --no-cache-dir gunicorn && pip install --no-cache-dir .

WORKDIR /app/src/webapp

EXPOSE 8000
CMD ["gunicorn", "--bind=0.0.0.0:8000", "app:app"]