import unittest
import points.model.map_point as map_point
import points.utils as utils
import os

#gpx_test_file_path = "/windows/ubuntu/gpx_data/2018-11-28 (09.17.27)/GPX/Archive/54.gpx"
gpx_test_file_path = "../data/67.gpx"
print(os.getcwd())

class MapPointTest(unittest.TestCase):
    def test_map_point_json(self):
        p = map_point.GpxPoint()

        p.id = 45
        p.elevation = 34.54
        p.gpx_file_id = 2
        p.latitude = 534.55
        p.longitude = 445.334
        p.course = 34.43
        p.time = utils.now()

        json = utils.to_json(p)

        p2 = map_point.GpxPoint.from_json_string(json)

        self.assertDictEqual(p.to_json_dict(), p2.to_json_dict())

    def test_from_dict(self):
        d = {
            "id": 35,
            "elevation": 35.35,
            "longitude": 98.4,
            "latitude": 98.2,
            "course": 998.2,
            "time": utils.datetime_to_string(utils.now()),
            "gpx_file_id": 5,
        }
        p = map_point.GpxPoint.from_dict(d)
        self.assertDictEqual(d, p.to_json_dict())


class GpxFileTest(unittest.TestCase):
    def test_json(self):
        g = map_point.GpxFile()
        g.id = 34
        g.gpx_timestamp = utils.now()
        g.parsed_time = utils.now()
        g.name = "fart"

        p = map_point.GpxPoint.from_dict({
            "id": 35,
            "elevation": 35.35,
            "longitude": 98.4,
            "latitude": 98.2,
            "course": 998.2,
            "time": utils.datetime_to_string(utils.now()),
        })
        g.points = [p]

        g2 = map_point.GpxFile.from_json_string(utils.to_json(g))

        self.assertDictEqual(g.to_json_dict(), g2.to_json_dict())

    def test_parse_gpx(self):
        path = gpx_test_file_path
        gpx_file = map_point.parse_gpx_file(path)
        self.assertGreater(len(gpx_file.points), 0)

    def redacted_test_find_gxp_files(self):
        path = "/windows/ubuntu/"
        gpx_files = map_point.find_gpx_files(path)
        self.assertGreater(len(gpx_files), 0)

    def test_flatten_points(self):
        path = gpx_test_file_path
        gpx_file = map_point.parse_gpx_file(path)

        for i, p in zip(gpx_file.flatten_points(), gpx_file.points):
            self.assertEqual(i.file_id, gpx_file.id)
            self.assertEqual(i.file_name, gpx_file.name)
            self.assertEqual(i.file_hash, gpx_file.hash)

            self.assertEqual(i.elevation, p.elevation)
            self.assertEqual(i.course, p.course)
            self.assertEqual(i.longitude, p.longitude)
            self.assertEqual(i.latitude, p.latitude)


class GpxFlatPointTest(unittest.TestCase):
    def test_json(self):
        n = utils.now()
        flat_point = map_point.GpxFlatPoint()
        flat_point.course = 1.0
        flat_point.longitude = 33.2
        flat_point.latitude = 228.3
        flat_point.elevation = 23.2
        flat_point.id = utils.create_uuid_str()
        flat_point.file_parsed_time = n
        flat_point.file_gpx_timestamp = n
        flat_point.time = n
        flat_point.file_id = 3
        flat_point.file_user_id = utils.create_uuid_str()
        flat_point.file_hash = "file_hash"
        flat_point.file_name = "file_name"

        json_data = utils.to_json(flat_point)
        flat_point2 = map_point.GpxFlatPoint.from_json_string(json_data)

        self.assertDictEqual(flat_point.__dict__, flat_point2.__dict__,
                             "expected flat point to serialize in and out of json as the same")


