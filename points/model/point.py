import json
import points.model.base as base
from sqlalchemy import Column, Integer, FLOAT, ForeignKey

Base = base.get_base()


class Point(Base):
    __tablename__ = "point"
    id = Column(Integer, primary_key=True)
    x = Column(FLOAT)
    y = Column(FLOAT)
    z = Column(FLOAT)
    point_set_id = Column(Integer, ForeignKey('point_set.id'))

    def __init__(self):
        Base.__init__(self)
        self.point_set_id = -1
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.id = None

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

    def set_point_set_id(self, id):
        self.point_set_id = id
        return self

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
