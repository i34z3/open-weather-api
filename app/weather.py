import requests

from flask import Flask, request, jsonify
from flask_caching import Cache

from dotenv import load_dotenv
load_dotenv()


app = Flask('app')


app.config.from_object('app.settings')
cache = Cache(app)

@app.route('/weather/<city>', methods=['GET'])
@cache.cached(timeout=300)
def weather(city):
    cache.set("city", city)
    url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s' % (city, app.config['API_KEY'])
    response = requests.get(url).json()
    return jsonify(response)


@app.route('/weather')
@cache.cached()
def get_cached():
    max_number = int(request.args.get('max'))
    if max_number > 5:
        return jsonify("Maximum of 5 entries by default.")
    cached_cities = cache.get("city")
    return jsonify(cached_cities)
