import sys
import os
import points.model.map_point as map_point
import points.pg.dao as dao_module
import points.pg.config as dao_config
from points.model.json import to_json


def create_output_fun(path: str):
    def f(gpx_file: map_point.GpxFile):
        json = gpx_file.to_json_string()
        user_id = gpx_file.user_id
        user_dir = "{path}/{user_id}".format(path=path, user_id=user_id)
        if not os.path.exists(user_dir):
            os.mkdir(user_dir, mode=755)

        path_to_write = "{user_dir}/{file_id}.json".format(user_dir=user_dir, file_id=gpx_file.hash)
        with open(path_to_write, 'w') as out:
            out.write(json)

    return f


def main():
    env = os.environ
    top_path = env["GPX_PATH"]

    if top_path is None or top_path == "":
        sys.stderr.write("no top path.  Exiting")
        os.exit(34)
    print(top_path)
    try:
        output_path = env["OUTPUT_DIR"]
    except KeyError:
        output_path = "json_files"

    if os.path.exists(output_path):
        os.rmdir(output_path)


    output_fun = create_output_fun(output_path)

    config = dao_config.Config.from_env(env)
    dao = dao_module.create_dao(config)
    u = dao.get_user(id=1)
    print(to_json(u))

    gpx_files = map_point.find_gpx_files(top_path)
    print("number of gpx files: {}".format(len(gpx_files)))

    for file in gpx_files:
        print("parsing: {}".format(file))
        p = map_point.parse_gpx_file(file)
        p.user_id = u.uuid
        print("persisting: {}, num points: {}".format(file, p.num_points()))
        dao.save_or_update_gpx_file(p)







if __name__ == "__main__": main()




