from flask import Flask, request

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def weather():
    zip_code = request.args.get('zip')
    if zip_code:
        weather_data = get_weather_data(zip_code)
        return weather_data, 200
    else:
        return 'Error: No zip code provided', 400

def get_weather_data(zip_code):
    if zip_code == '94560':
        weathearData = ' "weather": [{"description": "Clear Sky","temperature": "72","humidity": 30,"main": "Clear"}]'
    elif zip_code == '90001':
        weathearData = ' "weather": [{"description": "Rainy/FrezingRain","temperature": "80","humidity": 60,"main": "Rainy"}]'
    elif zip_code == '10001':
        weathearData = ' "weather": [{"description": "Snow Showers","temperature": "50","humidity": 50,"main": "Snow"}]'
    elif zip_code == '60601':
        weathearData = ' "weather": [{"description": "Partly Cloudy","temperature": "10","humidity": 10,"main": "Cloudy"}]'
    elif zip_code == '94550':
        weathearData = ' "weather": [{"description": "Mostly Sunny","temperature": "85","humidity": 20,"main": "Sunny"}]'
    else:
        weathearData ='No Information'
    
    return weathearData

if __name__ == '__main__':
    app.run()