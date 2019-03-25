import datetime
import json

class PointSet(object):
    def __init__(self):
        self.name = ""
        self.created = None
        self.id = -1
        self.points = []

    def __repr__(self):
        return ", ".join(["{}: {}".format(k, v) for k, v in self.__dict__.items()])


def now():
    return datetime.datetime.now()


