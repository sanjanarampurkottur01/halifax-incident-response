# Use an official Python runtime as a parent image
FROM python:3.9.13-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt 

# Expose the port the app runs on
EXPOSE 8050

# Run app.py when the container launches
CMD ["gunicorn", "-b", "0.0.0.0:8050", "app:server"]