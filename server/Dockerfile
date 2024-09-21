# Use an official Python image from the Docker Hub
# 3.12 chosen as it's what I have locally on my Macbook at the moment.
# See https://hub.docker.com/_/python
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY main.py .

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "main.py"]
