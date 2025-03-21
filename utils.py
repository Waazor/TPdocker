from datetime import datetime, timedelta

def day_on_month(date):
    year = str(date)[:4]
    month = str(date)[4:6]
    if month in {"01", "03", "05", "07", "08", "10", "12"}:
        return 31
    elif month == "02":
        if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
            return 29
        return 28
    else:
        return 30

def next_day(date_int):
    date_str = str(date_int)
    date_obj = datetime.strptime(date_str, '%Y%m%d')
    next_day_obj = date_obj + timedelta(days=1)
    return next_day_obj.strftime('%Y%m%d')

def past_day(date_int):

    date_str = str(date_int)
    date_obj = datetime.strptime(date_str, '%Y%m%d')
    next_day_obj = date_obj + timedelta(days=-1)
    return int(next_day_obj.strftime('%Y%m%d'))

def limite_date():
    date = datetime.today()
    past_date = date - timedelta(days=450)
    return past_date.strftime('%Y%m%d')

