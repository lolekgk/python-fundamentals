import math
from datetime import date, timedelta

import holidays


def estimate_date(start_date, estimated_hours):
    work_days = math.floor(estimated_hours / 8)
    holidays_list = holidays.PL(years=start_date.year).keys()
    current_date = start_date
    while work_days:
        weekday = current_date.isoweekday()
        if current_date.year != start_date.year:
            holidays_list = holidays.PL(years=current_date.year).keys()
        if weekday > 5 or current_date in holidays_list:
            current_date += timedelta(days=1)
            continue
        current_date += timedelta(days=1)
        work_days -= 1
    return current_date


start_date = date(2022, 7, 20)
print(start_date)
print(estimate_date(start_date, 8))
