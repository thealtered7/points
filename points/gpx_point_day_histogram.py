import points.model.map_point as map_point
import points.pg.dao as dao
import numpy as np
import points.model.utils as utils
import collections
import matplotlib
import matplotlib.pyplot as plt

def output_date_histogram(counter: collections.Counter):
    all_keys = sorted(counter.keys())
    fig = plt.figure()
    ax = fig.add_subplot(111)

def main():
    config = dao.config.Config.from_env(dao.config.get_development_env())
    pg_dao = dao.Dao.create_dao(config)

    with pg_dao.session_scope() as s:
        all_points = s.query(map_point.GpxPoint).options().all()

        counter = collections.Counter([utils.truncate_datetime_to_day(p.time) for p in all_points])
        all_keys = sorted(counter.keys())
        for k in all_keys:
            print("{}: {}".format(k, counter[k]))


        elevations = [p.elevation for p in all_points]
        longitudes = [p.longitude for p in all_points]
        latitudes = [p.latitude for p in all_points]

        max_elevation = max(elevations)
        min_elevation = min(elevations)
        max_long = max(longitudes)
        min_long = min(longitudes)
        max_lat = max(latitudes)
        min_lat = min(latitudes)


        print("min elevation: {}".format(min_elevation))
        print("max elevation: {}".format(max_elevation))
        print("min latitude: {}".format(min_lat))
        print("max latitude: {}".format(max_lat))
        print("min longitude: {}".format(min_long))
        print("max longitude: {}".format(max_long))

        output_date_histogram(counter)

if __name__ == "__main__": main()
