from flask import Flask, Response
from api_key import key
import requests
import json
from controllers import create_airQuality_controller, get_airQualities_controller
from airQuality import AirQuality

app = Flask(__name__)

r = requests.get("http://api.airvisual.com/v2/city?city=Warsaw&state=Mazovia&country=Poland&key=" + key).json()

pollution_data = r['data']['current']['pollution']
weather_data = r['data']['current']['weather']

air_quality = AirQuality()
air_quality.add_data({"pollution": pollution_data, "weather": weather_data})


@app.get('/')
def ping():
    return 'Welcome to the AirQuality API!'


@app.get('/airQualities')
def get_airQualities() -> Response:
    air_qualities = get_airQualities_controller.get()
    return Response(response=json.dumps(air_qualities), status=200, mimetype="application/json")


@app.get('/airQualities/create')
def create_airQuality() -> Response:
    try:
        create_airQuality_controller.create({
            "pollution": {
                "ts": air_quality._timestamp,
                "aqius": air_quality._aqi_US,
                "aqicn": air_quality._aqi_China,
                "mainus": air_quality._main_pollutant_US,
                "maincn": air_quality._main_pollutant_China
            },
            "weather": {
                "tp": air_quality._temperature,
                "pr": air_quality._athmospheric_pressure,
                "hu": air_quality._humidity,
                "ws": air_quality._wind_speed,
                "wd": air_quality._wind_direction
            }
        })
        return Response(response="AirQuality created", status=201)
    except ValueError as error:
        return Response(response=str(error), status=400)


@app.get('/airQualities/<string:timestamp>')
def get_airQuality(timestamp: str) -> Response:
    try:
        air_quality = get_airQualities_controller.get(timestamp=timestamp)
        return Response(response=json.dumps(air_quality), status=200, mimetype="application/json")
    except ValueError as error:
        return Response(response=str(error), status=400)


app.run(port=5001, debug=True)
