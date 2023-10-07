from datetime import datetime

def is_dark_outside(current_time, sunrise_time, sunset_time):
    return not (sunrise_time <= current_time < sunset_time)

sunrise_time = datetime.strptime('06:30', '%H:%M')
sunset_time = datetime.strptime('18:00', '%H:%M')

current_time = datetime.strptime('12:45', '%H:%M')

if is_dark_outside(current_time, sunrise_time, sunset_time):
    print("It is dark outside.")
else:
    print("It is not dark outside.")
