FROM ultralytics/yolov5:latest

# Copy model and application files
WORKDIR /app
COPY . /app

# Install additional dependencies (if needed)
RUN pip install -r requirements.txt

# Expose port 8000 for the Flask app
EXPOSE 8000

# Start the server
CMD ["python3", "app.py"]
