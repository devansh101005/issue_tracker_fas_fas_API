# Use official Python slim image (small size, has everything we need)
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first (Docker caches this layer separately)
# So if your code changes but requirements don't, pip install is skipped
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project code
COPY . .

# Create the data directory for issues.json persistence
RUN mkdir -p /app/data

# Tell Docker this container listens on port 8000
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
