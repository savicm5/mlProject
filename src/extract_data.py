import pandas as pd

def extract_hour_day_month(data):
    data['Hour'] = data['Date/Time'].dt.hour
    data['Month'] = data['Date/Time'].dt.month_name()
    data['Day'] = data['Date/Time'].dt.day
    data['DayOfWeek'] = data['Date/Time'].dt.day_name()

def extract_day_month(data):
    data['Month'] = data['Date/Time'].dt.month_name()
    data['Day'] = data['Date/Time'].dt.day
    data['DayOfWeek'] = data['Date/Time'].dt.day_name()