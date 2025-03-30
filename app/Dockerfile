# using lightweight python image
FROM --platform=linux/amd64 python:3.11-slim

# Create a non-root user
RUN addgroup --system appgroup && adduser --system --group appuser

WORKDIR /app
COPY requirements.txt app.py ./

# Installing  dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Changing ownership & add permissions
RUN chown -R appuser:appgroup /app

# Switching to non-root user
USER appuser

# Listening application on port
EXPOSE 3000

# Start the app
CMD ["python3", "app.py"]
