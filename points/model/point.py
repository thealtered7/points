
class Point(object):
    def __init__(self):
        self.point_set_id = -1
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

    def __repr__(self):
        return ", ".join(["{}: {}".format(k, v) for k, v in self.__dict__.items()])

    def __str__(self):
        return self.__repr__(self)
