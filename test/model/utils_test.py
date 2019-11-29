import unittest
import unittest.mock as mock
import os
import points.model.utils as utils


class UtilsTest(unittest.TestCase):

    def test_parse_gpx_timestamp(self):
        value = "2018-07-17T13:59:21Z"
        ts = utils.string_to_datetime(value)
        self.assertIsNotNone(ts, "gpx time stamp should not be null")

        ts_str = utils.datetime_to_string(ts)
        ts_copy = utils.string_to_datetime(ts_str)
        self.assertEqual(ts, ts_copy)

    def test_parse_float_or_none(self):
        input = "11.3"
        output = utils.parse_float_or_none(input)
        self.assertEqual(float(input), output)

        input = "gjleagj"
        output = utils.parse_float_or_none(input)
        self.assertIsNone(output)

        input = "435"
        output = utils.parse_float_or_none(input)
        self.assertEqual(float(input), output)

        input = None
        output = utils.parse_float_or_none(input)
        self.assertIsNone(output)

    def test_parse_int_or_none(self):
        input = "gjleagj"
        output = utils.parse_int_or_none(input)
        self.assertIsNone(output)

        input = "435"
        output = utils.parse_int_or_none(input)
        self.assertEqual(int(input), output)

        input = None
        output = utils.parse_float_or_none(input)
        self.assertIsNone(output)

    def test_move_directory(self):
        def everything_goes_well():
            self.datetime_to_string = utils.datetime_to_string
            mock_rename = mock.Mock()
            mock_datestring = mock.Mock()
            mock_datestring.return_value = "2019_01_01_00-00-00"
            self.rename = os.rename
            os.rename = mock_rename
            utils.datetime_to_string = mock_datestring

            input = "/a/file/path"
            expect = input + "-2019_01_01_00-00-00"
            ret = utils.move_directory(input)
            print(ret)
            self.assertEqual(expect, ret)

        [f() for f in [everything_goes_well]]

        utils.datetime_to_string = self.datetime_to_string
        os.rename = self.rename

    def test_md5_hash(self):
        output = utils.md5_hash("input")
        self.assertTrue(type(output) == str)

