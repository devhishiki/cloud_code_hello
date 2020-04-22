# Python image to use.
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# copy the requirements file used for dependencies
COPY ./src/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
