from models import Room, Timetable
import json
import datetime, time

def query_rooms():
    '''returns each room and its availability status'''
    response = []

    # loop through the rooms
    rooms = Room.get_all()

    if rooms:
        for r in rooms:
            # get current day/time stuff
            current_day = datetime.datetime.now().strftime('%A').lower()
            current_time = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')

            # get room use times
            room_times = Timetable.get_by_room_id(r.room_id)

            # determine usage
            use_flag = True
            for t in room_times:
                if t.day == current_day:
                    if (current_time >= t.start_time) and (current_time <= t.end_time):
                        use_flag = False
            response.append({"room_id": r.room_id, "room_number": r.room_number, "available": use_flag})
    else:
        response.append({})
    return response