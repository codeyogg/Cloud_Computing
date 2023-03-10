from pyzipcode import ZipCodeDatabase
from flask import Flask, request
import requests
app = Flask(__name__)
zcdb = ZipCodeDatabase()

@app.route('/', methods=['GET'])
def get_home():
    return "Hello! Browse to /zipcode.."

@app.route('/zipcode', methods=['GET'])
def get_zip_code():

    city = request.args.get('city')
    if city is None:
        return " Please provide a city name", 400
    
    matches = zcdb.find_zip(city=city)
    if matches is None or len(matches) == 0:
        return " Invalid city", 400

    # zip_code = f" Zip code for {city}  is {matches[0]}"
    zip_code = "" + matches[0].zip
    response = requests.get(f"http://svc2:5000/weather?zip={zip_code}")
    if response.status_code != 200:
      return "Failed to talk to svc2: ", response.status_code
    return response.text

  
if __name__ == '__main__':
    app.run()