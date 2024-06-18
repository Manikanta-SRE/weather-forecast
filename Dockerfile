FROM python:3.9-slim  # Use a slim Python base image

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "weather_app.py"]  # Replace "weather_app.py" with your script's name
