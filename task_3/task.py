import datetime


def date_difference(first_date: datetime.datetime, second_date: datetime.datetime) -> int:
    diff = (second_date - first_date).days
    if diff < 0:
        return abs(diff)
    else:
        return diff


first_time = datetime.datetime.now()
sec_time = datetime.datetime(year=2022, month=3, day=3)

print(type(date_difference(first_time, sec_time)))
