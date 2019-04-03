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

    def test_is_empty_string(self):
        self.assertTrue(point_utils.is_empty_string(None), "None should be an empty string")
        self.assertTrue(point_utils.is_empty_string(""), "'' should be an empty string")
        self.assertTrue(point_utils.is_empty_string("  "), "'  ' should be an empty string")
        self.assertFalse(point_utils.is_empty_string("I am not empty"), "populated string should not be empty")
