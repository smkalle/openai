# Use an official Python runtime as the parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install flask openai

# Specify the command to run the app
CMD ["python", "app.py"]

ENTRYPOINT python app.py


