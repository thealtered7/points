import os
import datetime
import dateutil.parser as parser
import os.path
import hashlib
import uuid
import json as js

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


def md5_hash(arg: str)-> str:
    arg = arg.encode('utf-8')
    algo = hashlib.md5()
    algo.update(arg)
    digest = algo.hexdigest()
    return digest


def create_uuid_str() -> str:
    return str(uuid.uuid4())


def move_directory(dir_path: str) -> str:
    dir_path = dir_path.rstrip("/")
    d = datetime_to_string(now()).replace(" ", "_").replace(":", "-").replace(".", "-")
    base_path, tail = os.path.split(dir_path)
    tail_name = tail + "-" + d
    move_to = os.path.join(base_path, tail_name)
    os.rename(dir_path, move_to)
    return move_to


def to_json(ob):
    """to_json takes an argument and calls to_json on it"""
    json_data = ob.to_json_dict()
    json_string = js.dumps(json_data, sort_keys=True, indent="\t")
    return json_string
