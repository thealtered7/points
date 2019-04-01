import unittest
import points.model.utils as point_utils


class TestDatetime(unittest.TestCase):
    def test_str(self):
        now = point_utils.now()
        print(now)
        now_string = point_utils.datetime_to_string(now)
        now_time = point_utils.string_to_datetime(now_string)
        print(now_string)
        self.assertEqual(now, now_time, "expected dates to parse and un-parse")


