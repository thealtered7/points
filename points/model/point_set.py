import datetime

class PointSet(object):
    def __init__(self):
        self.name = ""
        self.created = None
        self.id = -1
        self.points = []

def now():
    return datetime.datetime.now()