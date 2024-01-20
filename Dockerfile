# Use python:3 as the base image
FROM python:3

# Set the working directory for the application
WORKDIR /code

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Upgrade pip
RUN pip install --upgrade pip

# Install core dependencies
RUN apt-get update && apt-get install -y libpq-dev build-essential

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]