from datetime import datetime
import re

VTT_TIME_REGEX_PATTERN = "(\\d+):(\\d+):(\\d+).\\d+"


def get_date_time_string(date=datetime.today(), separator='_', date_separator='_', time_separator='_'):
    date_format = '%y' + date_separator + '%m' + date_separator + '%d'
    time_format = '%H' + time_separator + '%M' + time_separator + '%S'
    date_time_format = date_format + separator + time_format
    return date.strftime(date_time_format)


def parse_vtt_caption_to_seconds(time_str):
    m = re.match(VTT_TIME_REGEX_PATTERN, time_str)
    if m:
        hrs = int(m.group(1) or "0")
        mins = int(m.group(2) or "0")
        secs = int(m.group(3) or "0")
        return hrs*3600 + mins*60 + secs
    return 0
