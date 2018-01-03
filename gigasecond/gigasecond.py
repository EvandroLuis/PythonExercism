import datetime
GIGASECOND = 1000000000


def add_gigasecond(birth_date):
    return birth_date + datetime.timedelta(0, GIGASECOND)
