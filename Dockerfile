# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Upgrade pip
RUN /usr/local/bin/python -m pip install --upgrade pip

# Add requirements.txt file to the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Add the current directory contents into the container at /app
COPY . ./

# Run tests
# RUN python -m unittest discover -v

# Expose port
EXPOSE 5000

# Set Flask environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["flask", "run"]

