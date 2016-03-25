from app import db, models
import data_handler
import json

def fill_her_up():
	'''fills the database with data'''
	room_number = 'PG07'
	db.session.add(models.Room(room_number=room_number))
	db.session.flush() # this lets us magically get the primary key without committing the db session
	room = json.loads(data_handler.query_by_room_number(room_number))
	db.session.add(models.Timetable(room_id=room['room_id'], day='tuesday', start_time='12:00', end_time='13:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='wednesday', start_time='13:00', end_time='16:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='thursday', start_time='09:00', end_time='12:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='thursday', start_time='13:00', end_time='16:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='thursday', start_time='13:00', end_time='16:00'))

	room_number = 'PG04'
	db.session.add(models.Room(room_number=room_number))
	db.session.flush() # this lets us magically get the primary key without committing the db session
	room = json.loads(data_handler.query_by_room_number(room_number))
	db.session.add(models.Timetable(room_id=room['room_id'], day='monday', start_time='11:00', end_time='12:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='monday', start_time='13:00', end_time='14:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='monday', start_time='14:00', end_time='15:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='monday', start_time='16:00', end_time='17:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='tuesday', start_time='10:00', end_time='13:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='tuesday', start_time='14:00', end_time='15:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='tuesday', start_time='15:00', end_time='16:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='tuesday', start_time='16:00', end_time='17:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='wednesday', start_time='13:00', end_time='16:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='thursday', start_time='10:00', end_time='11:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='thursday', start_time='11:00', end_time='12:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='thursday', start_time='12:00', end_time='13:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='thursday', start_time='14:00', end_time='15:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='thursday', start_time='15:00', end_time='16:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='friday', start_time='10:00', end_time='11:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='friday', start_time='12:00', end_time='13:00'))
	db.session.add(models.Timetable(room_id=room['room_id'], day='friday', start_time='14:00', end_time='15:00'))

	db.session.commit()