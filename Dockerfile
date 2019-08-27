# Use an official Python runtime as a parent image
FROM python:3.7.4-alpine3.10

# Set the working directory to /app
WORKDIR /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV whoBuilt=Chase

#speed repeated builds of app code changes by building the requirement (which
# do not often change) at an earlier layer, thus not repeating the lengthy step every time
# this greatly decreases build time
COPY /requirements.txt /app

# Install any needed packages specified in requirements.txt with pyton pip package manager
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Run app.py when the container launches
CMD ["python", "app.py"]