#!/bin/bash
set -e

echo "Starting EduNexia API..."

# Run Alembic migrations
echo "Running database migrations..."
python -m alembic upgrade head

# Start the application
echo "Starting FastAPI server..."
exec uvicorn app.main:app --host 0.0.0.0 --port $PORT
