# Use an official Nginx runtime as the base image
FROM nginx:latest

# Set working directory within the container
WORKDIR /app

# Copy static content to the container
COPY static /app/static

# Install Python and pip for Flask application
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Flask
RUN pip3 install Flask

# Copy the Flask application code to the container
COPY app /app

# Expose port 80 for Nginx
EXPOSE 80

# Start Nginx and Flask application
CMD service nginx start && python3 app/app.py

