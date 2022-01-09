from datetime import datetime


def get_date_time_string(date=datetime.today(), separator='_', date_separator='_', time_separator='_'):
    date_format = '%y' + date_separator + '%m' + date_separator + '%d'
    time_format = '%H' + time_separator + '%M' + time_separator + '%S'
    date_time_format = date_format + separator + time_format
    return date.strftime(date_time_format)