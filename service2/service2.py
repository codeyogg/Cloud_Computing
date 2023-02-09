from flask import Flask, request
import requests, json

app = Flask(__name__)

api_key = '221ec055c8e6b0ae294773f1725c6539'
base_url = "http://api.openweathermap.org/data/2.5/weather?"


@app.route('/weather', methods=['GET'])
def weather():
    zip_code = request.args.get('zip')
    if zip_code:
        weather_data = get_weather_data(zip_code)
        return weather_data, 200
    else:
        return 'Error: No zip code provided', 400

def get_weather_data(zip_code):
    complete_url = base_url + "appid=" + api_key + "&q=" + zip_code
    response = requests.get(complete_url)
    rj = response.json()
    if rj["cod"] != "404":
        y = rj["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = rj["weather"]
        weather_description = z[0]["description"]
        return " Temperature (in kelvin unit) = " + str(current_temperature) + \
          "\n atmospheric pressure (in hPa unit) = " + str(current_pressure) + \
          "\n humidity (in percentage) = "  + str(current_humidity) + \
          "\n description = " + str(weather_description)
    else:
        return " Weather for Zipcode not found", 400

if __name__ == '__main__':
    app.run()