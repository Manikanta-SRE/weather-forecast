#Use the official Python Image
FROM python:3.9-slim

#set the working directory in the container
WORKDIR/app

#copy the pyhton dependencies file
COPY requirements.txt

#Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

#copy the Python script into the container 
COPY your_weather_forecast_script.py

#command to run the Python script
CMD ["python", "your_weather_forecast_script.py"]
