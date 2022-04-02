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
# api_key = app.config['API_KEY1']
# print(api_key)

@app.route('/news')
def news():
    country_name = request.args.get('country')
    api_key = app.config['API_KEY1']
    base_url = "http://newsapi.org/v2/top-headlines?"
    complete_url = base_url + "country=" + country_name + "&apiKey=" + api_key
    response = requests.get(complete_url)
    return response.json()

if __name__ == '__main__':
    app.run(host="0.0.0.0",port='3003',threaded=True,debug=True)