from flask import Flask, render_template, request, redirect, url_for
import requests
from datetime import datetime, timedelta
from dateutil import parser

app = Flask(__name__)

def format_datetime(value, format="%Y-%m-%d"):
    return datetime.utcfromtimestamp(value).strftime(format)

app.jinja_env.filters["datetime"] = format_datetime

def get_coordinates(location):
    print(location)
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1&language=en&format=json"
    print(url)
    response = requests.get(url)
    print(response.json())        
    try:
        results = requests.get(url).json()['results']
    except: 
        return None, None, None
    # results = data.get('results', [])
    else:
        result = results[0]
        coordinates = [result.get("longitude"), result.get("latitude")]
        place_name = result.get("name")
        country = result.get("country")
    
    if None in coordinates or place_name is None or country is None:
        return None, None, None

    return coordinates, place_name, country


def get_weather_forecast(latitude, longitude):
    print(latitude, longitude)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m&forecast_days=7&timezone=auto"
    print(url)
    response = requests.get(url)
    print(url)
    data = response.json()

    hourly_data = data['hourly']
    times = hourly_data['time']
    temperatures = hourly_data['temperature_2m']
    relative_humidities = hourly_data['relativehumidity_2m']

    forecast = {}

    for i, time in enumerate(times):
        dt = parser.parse(time)  
        date = dt.strftime('%Y-%m-%d')
        day = dt.strftime('%A')  
        hour = dt.hour

        if date not in forecast:
            forecast[date] = {"day": day, "day_max_temp": None, "night_max_temp": None, "day_max_humidity": None, "night_max_humidity": None}

        if hour == 6:
            # Updating day max temperature and humidity
            if forecast[date]["day_max_temp"] is None or temperatures[i] > forecast[date]["day_max_temp"]:
                forecast[date]["day_max_temp"] = temperatures[i]

            if forecast[date]["day_max_humidity"] is None or relative_humidities[i] > forecast[date]["day_max_humidity"]:
                forecast[date]["day_max_humidity"] = relative_humidities[i]

        elif hour == 18:
            # Updating day max temperature and humidity
            if forecast[date]["night_max_temp"] is None or temperatures[i] > forecast[date]["night_max_temp"]:
                forecast[date]["night_max_temp"] = temperatures[i]

            if forecast[date]["night_max_humidity"] is None or relative_humidities[i] > forecast[date]["night_max_humidity"]:
                forecast[date]["night_max_humidity"] = relative_humidities[i]

    last_date = (datetime.utcnow() + timedelta(days=7)).strftime('%Y-%m-%d')
    if last_date in forecast:
        del forecast[last_date]

    return forecast

@app.route("/", methods=["GET", "POST"])  
def index():
    if request.method == "POST":  
        location = request.form["location"]  
        coordinates, place_name, country = get_coordinates(location)  
        if coordinates:
            latitude = str(round(coordinates[1], 6))
            longitude = str(round(coordinates[0], 6))
            return redirect(url_for("weather", latitude=latitude, longitude=longitude, place_name=place_name, country=country))
        else:  
            return render_template("index.html", error="Location not found. Please try again")
    return render_template("index.html")



@app.route("/weather/<latitude>/<longitude>/<path:place_name>/<path:country>")
def weather(latitude, longitude, place_name, country):
    forecast_data = get_weather_forecast(latitude, longitude)
    return render_template("weather.html", place_name=place_name, country=country, forecast=forecast_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
