import datetime
import points.model.point as point
import points.model.utils as p_utils
import json
import points.model.base as base
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship, backref

Base = base.get_base()


class PointSet(Base):
    __tablename__ = "point_set"
    id = Column(Integer, primary_key=True)
    created = Column(TIMESTAMP, nullable=False)
    name = Column(String, nullable=False)
    points = relationship(point.Point, backref=backref('point', uselist=True, cascade="delete,all"))

    def __init__(self):
        Base.__init__(self)
        self.name = ""
        self.created = None
        self.id = None
        self.points = []

    def __repr__(self):
        return ", ".join(["{}: {}".format(k, v) for k, v in self.__dict__.items()])

    def number_of_points(self):
        if self.points is None:
            return 0
        else:
            return len(self.points)

    def copy_of_points(self):
        if self.points is None:
            return []
        else:
            return [x for x in self.points]

    def to_json_dict(self):
        created_at_string = p_utils.datetime_to_string(self.created)
        data = {
            "name": self.name,
            "id": self.id,
            "created": created_at_string,
            "points": [x.to_json_dict() for x in self.points]
        }

        return data

    def from_dict(data):
        created_at_string = data["created"]
        created_at = p_utils.string_to_datetime(created_at_string)

        point_set = PointSet()
        point_set.name = data["name"]
        point_set.id = data["id"]
        point_set.created = created_at
        point_set.points = [point.Point.from_dict(p) for p in data["points"]]

        return point_set

    def from_json(data):
        json_dict = json.loads(data)
        point_set = PointSet.from_dict(json_dict)
        return point_set

