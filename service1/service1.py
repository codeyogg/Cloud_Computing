from flask import Flask, request
app = Flask(__name__)

@app.route('/zipcode', methods=['GET'])
def get_zip_code():
    
    ZIP_CODES = {
    "New York": "10001",
    "Los Angeles": "90001",
    "Chicago": "60601",
    "Newark" : "94560"
}

    city = request.args.get('city')
    if city is None:
        return " Please provide a city name", 400
    zip_code = f" Zip code for {city}  is {ZIP_CODES.get(city)}"
    if zip_code is None:
        return f" Zip code for {city} not found", 404
    return zip_code

if __name__ == '__main__':
    app.run()