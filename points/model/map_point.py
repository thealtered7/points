import json
import points.model.base as base
import points.model.utils as utils
from sqlalchemy import Column, Integer, Float, ForeignKey, TIMESTAMP

Base = base.get_base()

class GpxPoint(Base):
    __tablename__ = "gpx_point"
    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    altitude = Column(Float)
    heading = Column(Float)
    time = Column(TIMESTAMP)

    def __init__(self):
        Base.__init__(self)

    def to_json_dict(self):
        #todo add time
        return {
            "id": self.id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "altitude": self.altitude,
            "header": self.heading,
            "time": utils.datetime_to_string(self.time),
        }

    def from_dict(data):
        #TODO
        assert False, "from_dict not implemented"
        p = GpxPoint(data)
        return p

    def from_json_string(data):
        dictionary = json.loads(data)
        p = GpxPoint.from_dict(dictionary)
        return p

    def __repr__(self):
        json_dict = self.to_json_dict()
        return json.dumps(json_dict)

    def __str__(self):
        return self.__repr__()
