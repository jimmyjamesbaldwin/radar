from app import app, db, models
import data_handler
import json

@app.route('/api/')
def return_welcome():
    return '{"message": "welcome to the api. please read the documentation for usage"}'

@app.route('/api/room/')
def test():
	return json.dumps(data_handler.query_rooms())