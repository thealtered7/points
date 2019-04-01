import json

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

    def to_json_dict(self):
        return {
            "point_set_id": self.point_set_id,
            "x": self.x,
            "y": self.y,
            "z": self.z
        }

    def from_dict(data):
        p = Point()
        p.point_set_id = data["point_set_id"]
        p.x = data["x"]
        p.y = data["y"]
        p.z = data["z"]

        return p

    def from_json_string(data):
        dictionary = json.loads(data)
        p = Point.from_dict(dictionary)
        return p
