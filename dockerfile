# Set the base image
FROM python:3.10.8

# Define the working directory inside the container
WORKDIR /app

# Copy the source code to the working directory
COPY . .

# Install project dependencies
RUN pip install --no-cache-dir -r ./lib/requirements.txt

# Define the API execution command
CMD ["python", "main.py"]