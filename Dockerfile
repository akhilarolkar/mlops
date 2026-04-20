# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy just the requirements first to leverage Docker layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code AND the model.pkl file
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Tell Docker how to run your application
CMD ["python", "app.py"]