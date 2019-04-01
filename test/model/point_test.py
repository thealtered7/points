import points.model.point as point
import unittest


class PointTest(unittest.TestCase):

    def test_to_json_dict(self):
        p = point.Point()
        p.x = 3.0
        p.y = 5.0
        p.z = 7.0
        p.point_set_id = 45

        data = p.to_json_dict()

        self.assertEqual(p.x, data["x"], "expected x value to be equal")
        self.assertEqual(p.y, data["y"], "expected y value to be equal")
        self.assertEqual(p.z, data["z"], "expected z value to be equal")
        self.assertEqual(p.point_set_id, data["point_set_id"], "expected point_set_id value to be equal")

    def test_from_json_dict(self):
        data = {
            "x": 0.4,
            "y": 0.2,
            "z": 05.40,
            "point_set_id": 45
        }

        p = point.Point.from_dict(data)
        self.assertEqual(p.x, data["x"], "expected x value to be equal")
        self.assertEqual(p.y, data["y"], "expected y value to be equal")
        self.assertEqual(p.z, data["z"], "expected z value to be equal")
        self.assertEqual(p.point_set_id, data["point_set_id"], "expected point_set_id value to be equal")

    def test_from_json_string(self):
        json_string = """{"x": 3.4, "y": 52.4, "z": 45.35, "point_set_id": 45}"""

        p = point.Point.from_json_string(json_string)
        self.assertEqual(p.x, 3.4, "expected x value to be equal")
        self.assertEqual(p.y, 52.4, "expected y value to be equal")
        self.assertEqual(p.z, 45.35, "expected z value to be equal")
        self.assertEqual(p.point_set_id, 45, "expected point_set_id value to be equal")


if __name__ == "__main__":
    unittest.main()
