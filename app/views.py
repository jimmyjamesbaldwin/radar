from flask import render_template, flash, redirect
from app import app, db, models
import json
import data_handler

@app.after_request
def apply_caching(response):
    '''hide the app version from anything being nosey'''
    response.headers["Server"] = ""
    return response

@app.route('/rooms')
def rooms():
	return render_template('map.html', room_data=json.dumps(data_handler.query_rooms())) 

@app.route('/api/')
def return_welcome():
    return '{"message": "welcome to the api. please read the documentation for usage"}'

@app.route('/api/rooms/')
def api_rooms():
	return json.dumps(data_handler.query_rooms())