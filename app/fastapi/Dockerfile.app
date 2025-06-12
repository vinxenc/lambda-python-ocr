FROM python:3.12-slim

WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install the specified packages
RUN pip install -r requirements.txt

# Copy application code
COPY app.py .

# Expose port for the FastAPI application
EXPOSE 8000

# Command to run the application using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]