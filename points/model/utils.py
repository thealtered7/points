import datetime
import dateutil.parser as parser
import os.path
import hashlib
import uuid

ISO_8601 = "2008-09-03T20:56:35.450686"


def now():
    return datetime.datetime.now()


def datetime_to_string(dt):
    return dt.isoformat()


def string_to_datetime(s):
    return parser.parse(s)


def is_empty_string(inArg):
    return inArg is None or inArg.strip() == ""


def parse_float_or_none(arg):
    try:
        ret = float(arg)
    except ValueError:
        ret = None
    except TypeError:
        ret = None

    return ret


def parse_int_or_none(arg):
    try:
        ret = int(arg)
    except ValueError:
        ret = None
    except TypeError:
        ret = None

    return ret


def get_file_name_from_path(path: str) -> str:
    return os.path.basename(path)


def truncate_datetime_to_day(ts: datetime.datetime) -> datetime.datetime:
    copy = datetime.datetime(ts.year, ts.month, ts.day, 0, 0, 0, 0, ts.tzinfo)
    return copy


def truncate_datetime_to_month(ts: datetime.datetime) -> datetime.datetime:
    copy = datetime.datetime(ts.year, ts.month, 1, 0, 0, 0, 0, ts.tzinfo)
    return copy


def md5_hash(arg):
    algo = hashlib.md5()
    algo.update(arg)
    digest = algo.digest()
    return str(digest)


def create_uuid_str():
    return str(uuid.uuid4())
