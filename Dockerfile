# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy files into the container and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# This 
RUN mkdir -p /app/output

# Default command to run the scraper
CMD ["python", "scraper.py"]