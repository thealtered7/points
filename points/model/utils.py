import datetime
import dateutil.parser as parser

ISO_8601 = "2008-09-03T20:56:35.450686"


def now():
    return datetime.datetime.now()


def datetime_to_string(dt):
    return dt.isoformat()


def string_to_datetime(s):
    return parser.parse(s)


def is_empty_string(inArg):
    return inArg is None or inArg.strip() == ""

