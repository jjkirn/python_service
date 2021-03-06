from distutils.command.config import config
from flask import Flask, request
from flask_restful import Resource, Api, reqparse 
from json import dumps
from flask import jsonify
import json
import requests
# import config

app = Flask(__name__)
app.config.from_object('config.DevConfig')
api = Api(app)
# print(app.config['API_KEY2'])
# print(api_key)

@app.route('/weather')
def weather():
    city_name = request.args.get('city')
    api_key = app.config['API_KEY2']
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    return response.json()

if __name__ == '__main__':
     app.run(host="0.0.0.0",port='3002',threaded=True,debug=True)