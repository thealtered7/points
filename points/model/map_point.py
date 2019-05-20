import json
import points.model.base as base
import points.model.utils as utils
from sqlalchemy import Column, Integer, Float, ForeignKey, TIMESTAMP, String
from sqlalchemy.orm import relationship, backref
import xmltodict
import os
import collections

Base = base.get_base()

class GpxPoint(Base):
    __tablename__ = "gpx_point"
    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)
    course = Column(Float)
    time = Column(TIMESTAMP)
    gpx_file_id = Column(Integer, ForeignKey('gpx_file.id'))

    def __init__(self):
        Base.__init__(self)

    def to_json_dict(self):
        return {
            "id": self.id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "elevation": self.elevation,
            "course": self.course,
            "time": utils.datetime_to_string(self.time),
            "gpx_file_id": self.gpx_file_id,
        }

    def from_dict(data):
        p = GpxPoint()
        try:
            p.id = data["id"]
        except KeyError:
            p.id = None

        p.time = utils.string_to_datetime(data["time"])
        p.latitude = utils.parse_float_or_none(data["latitude"])
        p.longitude = utils.parse_float_or_none(data["longitude"])
        try:
            p.gpx_file_id = utils.parse_int_or_none(data["gpx_file_id"])
        except KeyError:
            p.gpx_file_id = None

        p.course = utils.parse_float_or_none(data["course"])
        p.elevation = utils.parse_float_or_none(data["elevation"])

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


class GpxFile(Base):
    __tablename__ = "gpx_file"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gpx_timestamp = Column(TIMESTAMP, nullable=False)
    parsed_time = Column(TIMESTAMP, nullable=False)
    points = relationship(GpxPoint, backref=backref('gpx_point', uselist=True, cascade="delete,all"))

    def __init__(self):
        Base.__init__(self)

    def to_json_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "gpx_timestamp": utils.datetime_to_string(self.gpx_timestamp),
            "parsed_time": utils.datetime_to_string(self.parsed_time),
            "points": [u.to_json_dict() for u in self.points],
        }

    def from_dict(data):
        gpx_file = GpxFile()
        try:
            gpx_file.id = utils.parse_int_or_none(data["id"])
        except KeyError:
            gpx_file.id = None

        gpx_file.parsed_time = utils.string_to_datetime(data["parsed_time"])
        gpx_file.gpx_timestamp = utils.string_to_datetime(data["gpx_timestamp"])
        gpx_file.name = data["name"]
        gpx_file.points = [GpxPoint.from_dict(x) for x in data["points"]]

        return gpx_file

    def from_json_string(data):
        dictionary = json.loads(data)
        p = GpxFile.from_dict(dictionary)
        return p

    def num_points(self):
        return len(self.points)

def find_gpx_files(path):
    gpx_paths = []
    def is_gpx_file(name: str) -> bool:
        return name.endswith("gpx")

    for root, dirs, files in os.walk(path):
        for file in files:
            if is_gpx_file(file):
                gpx_paths.append(os.path.join(root, file))

    return gpx_paths

def parse_gpx_file(file_name: str):
    with open(file_name) as input_stream:
        xml_data = input_stream.read(-1)
        xml_dict = xmltodict.parse(xml_data)
        gpx = xml_dict["gpx"]

        time_created = gpx["metadata"]["time"]
        track_data = gpx["trk"]
        if type(track_data) != list:
            track_data = [track_data]

        all_points = []

        for current_track in track_data:
            track_segments = current_track["trkseg"]
            for segment in track_segments:
                if type(segment) == collections.OrderedDict:
                    point_list = segment["trkpt"]
                    for point in point_list:
                        extensions = point["extensions"]["gpxtpx:TrackPointExtension"]
                        course = extensions["gpxtpx:course"]
                        p = GpxPoint()
                        p.longitude = utils.parse_float_or_none(point["@lon"])
                        p.latitude = utils.parse_float_or_none(point["@lat"])
                        p.elevation = utils.parse_float_or_none(point["ele"])
                        p.time = utils.string_to_datetime(point["time"])
                        p.course = utils.parse_float_or_none(course)
                        all_points.append(p)

        gpx_file = GpxFile()
        gpx_file.name = utils.get_file_name_from_path(file_name)
        gpx_file.parsed_time = utils.now()
        gpx_file.gpx_timestamp = utils.string_to_datetime(time_created)
        gpx_file.points = all_points
        return gpx_file
