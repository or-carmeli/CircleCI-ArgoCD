# Stage 1: Build and Test
FROM python:3.9-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Install testing dependencies (if not included in requirements.txt)
RUN pip install pytest
COPY . .
# Run tests
RUN python -m unittest discover -v

# Stage 2: Production Build
FROM python:3.9-slim
WORKDIR /app
# Copy only necessary artifacts from builder stage
COPY --from=builder /app /app
EXPOSE 5000
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["python3", "app.py"]
