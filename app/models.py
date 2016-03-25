from app import db
from sqlalchemy import UniqueConstraint


class Room(db.Model):
    __tablename__ = 'tbl_room'
    room_id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(50), nullable=False, unique=True)

    @staticmethod
    def get_all():
        return Room.query.all()


class Timetable(db.Model):
    __tablename__ = 'tbl_timetable'
    booking_id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('tbl_room.room_id'), nullable=False)
    day = db.Column(db.String(9), nullable=False)
    start_time = db.Column(db.String(5), nullable=False)
    end_time = db.Column(db.String(5), nullable=False)

    @staticmethod
    def get_by_room_id(id):
        return Timetable.query.filter_by(room_id=id).all()
