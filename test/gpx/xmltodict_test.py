import unittest
import xmltodict
import points.model.map_point as gpx_point
import os
import points.utils as utils

class XmlToDictText(unittest.TestCase):
    def test_xmltodict(self):
        to_parse = os.environ["DATA_FILE"]
        with open(to_parse) as input_stream:
            xml_data = input_stream.read(-1)
            xml_dict = xmltodict.parse(xml_data)
            self.assertGreaterEqual(len(xml_dict), 0, "expected xml dictionary to be greater than 0")

            gpx = xml_dict["gpx"]

            time_created = gpx["metadata"]["time"]

            track_data = gpx["trk"]
            segment_name = track_data["name"]

            print("time created: {}".format(time_created))
            print("segment name: {}".format(segment_name))

            track_segments = track_data["trkseg"]

            all_points = []
            for segment in track_segments:
                point_list = segment["trkpt"]
                for point in point_list:
                    extensions = point["extensions"]["gpxtpx:TrackPointExtension"]
                    course = extensions["gpxtpx:course"]
                    p = gpx_point.GpxPoint()
                    p.longitude = point["@lon"]
                    p.latitude = point["@lat"]
                    p.elevation = point["ele"]
                    p.time = utils.string_to_datetime(point["time"])
                    p.course = course
                    all_points.append(p)

            print("number of points parsed {}".format(len(all_points)))
            print(all_points[0])




