# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy files into the container and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# This will copy the entire python script. Make sure it is complete
COPY scraper.py .

# This 
RUN mkdir -p /app/output

# Default command to run the scraper
CMD ["python", "scraper_try.py"]