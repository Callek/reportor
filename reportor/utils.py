import calendar

def td2s(td):
    """Converts a `datetime.timedelta` into seconds"""
    return (td.days * 86400 + td.seconds + td.microseconds / 1000000.0)

def dt2ts(dt):
    """Converts a datetime object to a epoch timestamp. Assumes that the datetime object is already in UTC time."""
    return calendar.timegm(dt.utctimetuple())
