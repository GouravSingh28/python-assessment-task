FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy server code
COPY server.py .

# Expose port 80
EXPOSE 80

# Run the server
CMD ["python", "server.py"]
