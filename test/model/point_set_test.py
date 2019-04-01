import points.model.point as point
import points.model.point_set as point_set
import points.model.utils as point_utils
import unittest

class TestPointSet(unittest.TestCase):

    def test_point_set_number_of_points(self):
        ps = point_set.PointSet()
        self.assertEqual(ps.number_of_points(), 0, "expected number_of_points to be 0 on newly instantiated point_set")

        ps.points = None
        self.assertEqual(ps.number_of_points(), 0, "expected number_of_points to be 0 on point_set.points is None")

        ps.points = [point.Point()]
        self.assertEqual(ps.number_of_points(), 1, "expected number_of_points to be 1 after adding a point")

    def test_point_set_to_dict(self):
        ps = point_set.PointSet()
        ps.created = point_utils.now()
        ps.name = "Test Case"
        ps.id = 448

        point_one = point.Point.from_dict({
            "x": 409.39,
            "y": 348.44,
            "z": 54.33,
            "point_set_id": 448
        })

        ps.points = [point_one]

        data = ps.to_json_dict()
        date_string = data["created"]
        date_time = point_utils.string_to_datetime(date_string)

        self.assertEqual(data["id"], ps.id, "expected the id to be the same")
        self.assertEqual(data["name"], ps.name, "expected the name to be the same")
        self.assertEqual(date_time, ps.created, "expected created at date to match")

    def test_point_set_from_dict(self):
        now = point_utils.now()
        dict_data = {
            "id": 34,
            "created": point_utils.datetime_to_string(now),
            "name": "Test Case Point Set Is Fantastic",
            "points": [
                {
                    "x": 3.4,
                    "y": 4.2,
                    "z": 54.3,
                    "point_set_id": 34
                },
                {
                    "x": 3.6,
                    "y": 4.3,
                    "z": 54.5,
                    "point_set_id": 34
                }
            ]
        }

        ps = point_set.PointSet.from_dict(dict_data)

        self.assertEqual(ps.id, 34, "expected id to match")
        self.assertEqual(ps.name, "Test Case Point Set Is Fantastic", "expected name to match")
        self.assertEqual(ps.created, now, "expected created to match")
        self.assertEqual(ps.number_of_points(), 2, "expected point count to match")
        self.assertEqual([p.point_set_id for p in ps.points], [34, 34], "expected the point set ids to match")
        self.assertEqual([p.x for p in ps.points], [3.4, 3.6], "expected the x values to match")
        self.assertEqual([p.y for p in ps.points], [4.2, 4.3], "expected the y values to match")
        self.assertEqual([p.z for p in ps.points], [54.3, 54.5], "expected the z values to match")

