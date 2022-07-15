from datetime import datetime, timedelta


def count_days(start_date, end_date):
    """Counts number of days between two dates"""
    delta = start_date - end_date
    return abs(delta.days)


def date_from(start_date, days):
    """Returns new date that is x days away from the given date"""
    return start_date + timedelta(days=days)


start_date = datetime.strptime("15-07-2022", "%d-%m-%Y")
end_date = datetime.strptime("01-07-2022", "%d-%m-%Y")
days = -10
print(count_days(start_date, end_date))
print(date_from(start_date, days))
