import os
import points.model.map_point as map_point
import points.pg.dao as dao_module
import points.pg.config as dao_config


def main():
    env = os.environ
    top_path = env["GPX_PATH"]

    config = dao_config.Config.from_env(env)
    dao = dao_module.create_dao(config)

    gpx_files = map_point.find_gpx_files(top_path)

    for file in gpx_files:
        print("parsing: {}".format(file))
        p = map_point.parse_gpx_file(file)
        print("persisting: {}, num points: {}".format(file, p.num_points()))
        dao.save_or_update_gpx_file(p)







if __name__ == "__main__": main()




