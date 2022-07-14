import math
from datetime import date, timedelta

WORK_DAY_HOURS = 8


def estimate_date(start_date, estimated_hours):
    start_date = date.fromisoformat(start_date)
    work_days = math.ceil(estimated_hours / WORK_DAY_HOURS)
    end_time = start_date + timedelta(work_days)
    return work_days, end_time
