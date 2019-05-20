import unittest
import points.model.map_point as map_point
import points.model.utils as utils
import points.model.json as p_json


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

        json = p_json.to_json(p)

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

        g2 = map_point.GpxFile.from_json_string(p_json.to_json(g))

        self.assertDictEqual(g.to_json_dict(), g2.to_json_dict())

    def test_parse_gpx(self):
        path = "/windows/ubuntu/gpx_data/2018-11-28 (09.17.27)/GPX/Archive/54.gpx"
        gpx_file = map_point.parse_gpx_file(path)
        print(len(gpx_file.points))

    def redacted_test_find_gxp_files(self):
        path = "/windows/ubuntu/"
        gpx_files = map_point.find_gpx_files(path)
        self.assertGreater(len(gpx_files), 0)



