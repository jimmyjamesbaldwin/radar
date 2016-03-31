from flask import render_template, flash, redirect
from app import app, db, models
import json
import data_handler

@app.after_request
def apply_caching(response):
    '''hide the app version from anything being nosey'''
    response.headers["Server"] = ""
    return response

# ------------------------
# view controller routes
# ------------------------
@app.route('/')
@app.route('/index')
def rooms():
	try:
		room_data = json.dumps(data_handler.query_rooms())
	except Exception as e:
		return server_error(e)
		
	return render_template('map.html', room_data=json.dumps(data_handler.query_rooms()))

# ------------------------
# api routes
# ------------------------
@app.route('/api')
def return_welcome():
    return '{"message": "welcome to the api. please read the documentation for usage"}'

@app.route('/api/rooms')
def api_rooms():
	try:
		return json.dumps(data_handler.query_rooms())
	except Exception as e:
		return '{"error": ' + e + '}'

# ------------------------
# error handling
# ------------------------
@app.errorhandler(404)
def server_error(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500