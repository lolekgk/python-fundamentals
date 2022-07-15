import math
from datetime import date, datetime, timedelta

WORKING_HOURS = 8


def estimate_date(start_date, estimated_hours):
    # start_date = date.fromisoformat(start_date)
    start_date = datetime.strptime(start_date, "%d/%m/%Y")
    work_days = math.ceil(estimated_hours / WORKING_HOURS)
    task_end_date = (start_date + timedelta(work_days)).strftime("%d/%m/%Y")
    return work_days, task_end_date


if __name__ == '__main__':
    # work_days, task_end_date = estimate_date(str(date.today()), 10)
    work_days, task_end_date = estimate_date("15/07/2022", 10)
    print(f'Work days needed to finish the task: {work_days}.')
    print(f'Estimated end date of task: {task_end_date}.')


# We can also use datetime.strptime() to convert specyfic string format to datetime object
