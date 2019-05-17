import xmltodict
import points.model.map_point as gpx_point
import points.model.utils as utils


def parse_gpx_file(file_name: str):
    with open(file_name) as input_stream:
        xml_data = input_stream.read(-1)
        xml_dict = xmltodict.parse(xml_data)
        gpx = xml_dict["gpx"]

        time_created = gpx["metadata"]["time"]
        track_data = gpx["trk"]
        segment_name = track_data["name"]
        track_segments = track_data["trkseg"]

        all_points = []
        for segment in track_segments:
            point_list = segment["trkpt"]
            for point in point_list:
                extensions = point["extensions"]["gpxtpx:TrackPointExtension"]
                course = extensions["gpxtpx:course"]
                p = gpx_point.GpxPoint()
                p.longitude = utils.parse_float_or_none(point["@lon"])
                p.latitude = utils.parse_float_or_none(point["@lat"])
                p.altitude = utils.parse_float_or_none(point["ele"])
                p.time = utils.string_to_datetime(point["time"])
                p.heading = utils.parse_float_or_none(course)
                all_points.append(p)

        return all_points

