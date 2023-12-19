# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Add the current directory contents into the container at /app
COPY . .

# Expose port
EXPOSE 5000

# Set Flask environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["python3", "app.py"]
