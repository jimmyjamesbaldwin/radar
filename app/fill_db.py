from app import db, models
import data_handler
import json

def fill_her_up():
        '''fills the database with data'''

        room_number = 'P235'
        db.session.add(models.Room(room_number=room_number))
        db.session.flush() # this lets us magically get the primary key without committing the db session
        room = models.Room.get_by_room_number(room_number)
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='15:00', end_time='16:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='17:00', end_time='18:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='tuesday', start_time='12:00', end_time='13:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='tuesday', start_time='15:00', end_time='16:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='tuesday', start_time='17:00', end_time='18:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='thursday', start_time='12:00', end_time='13:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='thursday', start_time='15:00', end_time='16:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='friday', start_time='12:00', end_time='13:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='friday', start_time='13:00', end_time='14:00'))

        room_number = 'P234'
        db.session.add(models.Room(room_number=room_number))
        db.session.flush() # this lets us magically get the primary key without committing the db session
        room = models.Room.get_by_room_number(room_number)
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='09:00', end_time='10:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='11:00', end_time='12:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='13:00', end_time='18:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='tuesday', start_time='10:00', end_time='13:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='tuesday', start_time='14:00', end_time='18:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='wednesday', start_time='12:00', end_time='13:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='thursday', start_time='10:00', end_time='12:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='thursday', start_time='15:00', end_time='17:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='friday', start_time='09:00', end_time='16:00'))

        room_number = 'P233'
        db.session.add(models.Room(room_number=room_number))
        db.session.flush() # this lets us magically get the primary key without committing the db session
        room = models.Room.get_by_room_number(room_number)
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='09:00', end_time='12:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='13:00', end_time='18:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='tuesday', start_time='09:00', end_time='13:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='tuesday', start_time='14:00', end_time='16:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='tuesday', start_time='17:00', end_time='18:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='wednesday', start_time='13:00', end_time='15:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='thursday', start_time='10:00', end_time='12:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='thursday', start_time='14:00', end_time='16:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='friday', start_time='09:00', end_time='13:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='friday', start_time='14:00', end_time='15:00'))

        room_number = 'P230'
        db.session.add(models.Room(room_number=room_number))
        db.session.flush() # this lets us magically get the primary key without committing the db session
        room = models.Room.get_by_room_number(room_number)
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='11:00', end_time='12:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='13:00', end_time='15:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='16:00', end_time='17:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='tueday', start_time='10:00', end_time='13:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='tueday', start_time='14:00', end_time='16:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='wednesday', start_time='13:30', end_time='16:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='thursday', start_time='13:00', end_time='14:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='thursday', start_time='15:00', end_time='17:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='friday', start_time='09:00', end_time='15:00'))

        room_number = 'P227'
        db.session.add(models.Room(room_number=room_number))
        db.session.flush() # this lets us magically get the primary key without committing the db session
        room = models.Room.get_by_room_number(room_number)
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='11:00', end_time='18:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='tuesday', start_time='10:00', end_time='13:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='tuesday', start_time='14:00', end_time='17:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='thursday', start_time='09:00', end_time='14:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='thursday', start_time='15:00', end_time='16:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='friday', start_time='09:00', end_time='15:00'))

        room_number = 'P202'
        db.session.add(models.Room(room_number=room_number))
        db.session.flush() # this lets us magically get the primary key without committing the db session
        room = models.Room.get_by_room_number(room_number)
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='09:00', end_time='10:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='11:00', end_time='12:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='13:00', end_time='18:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='tuesday', start_time='09:00', end_time='17:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='tuesday', start_time='18:00', end_time='19:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='wednesday', start_time='09:00', end_time='13:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='thursday', start_time='09:00', end_time='18:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='fruday', start_time='09:00', end_time='16:00'))

        room_number = 'P203'
        db.session.add(models.Room(room_number=room_number))
        db.session.flush() # this lets us magically get the primary key without committing the db session
        room = models.Room.get_by_room_number(room_number)
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='09:00', end_time='10:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='11:00', end_time='12:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='13:00', end_time='15:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='monday', start_time='16:00', end_time='18:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='tuesday', start_time='09:00', end_time='13:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='tuesday', start_time='14:00', end_time='18:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='wednesday', start_time='09:00', end_time='10:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='wednesday', start_time='11:00', end_time='14:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='thursday', start_time='12:00', end_time='14:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='thursday', start_time='15:00', end_time='17:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='friday', start_time='09:00', end_time='13:00'))
        db.session.add(models.Timetable(room_id=room.room_id, day='friday', start_time='14:00', end_time='15:00'))

        db.session.commit()
