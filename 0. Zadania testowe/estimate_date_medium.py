import math
from datetime import date, timedelta

import holidays


def estimate_date(start_date, estimated_hours):
    work_days = math.ceil(estimated_hours / 8)
    holidays_data = holidays.PL(years=start_date.year).keys()
    days_to_add = work_days
    current_date = start_date

    while days_to_add:
        weekday = current_date.isoweekday()
        current_date += timedelta(days=1)
        if current_date.year != start_date.year:
            holidays_data = holidays.PL(years=current_date.year).keys()
        if weekday > 5 or current_date in holidays_data:
            continue
        days_to_add -= 1

    return work_days, current_date


start_date = date(2022, 10, 31)
work_days, end_date = estimate_date(start_date, 9)
print(work_days, end_date)
