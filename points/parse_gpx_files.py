import sys
import os
import points.model.map_point as map_point
import points.pg.dao as dao_module
import points.pg.config as dao_config
import points.model.utils as utils
import points.logging_utils as logging_utils

logging_utils.init()
logger = logging_utils.create_logger("parse_gpx_files")


from points.model.json import to_json

"""This file parses a directory of gpx files and saves them to postgres."""
def create_output_fun(path: str):
    def f(gpx_file: map_point.GpxFile):
        json = to_json(gpx_file)
        user_id = gpx_file.user_id
        user_dir = "{path}/{user_id}".format(path=path, user_id=user_id)
        if not os.path.exists(user_dir):
            os.mkdir(user_dir, mode=0o755)

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
    logger.info("path to gpx_files", extra=logging_utils.wrap_props({"directory": top_path}))

    config = dao_config.Config.from_env(env)
    dao = dao_module.create_dao(config)
    parse_files = []
    with dao.session_scope() as session:
        u = dao_module.get_user(session)(id=1)
        logger.info("user", extra={"props": u.to_json_dict()})

        gpx_files = map_point.find_gpx_files(top_path)
        logger.info("number of gpx files", extra=logging_utils.wrap_props({"count": len(gpx_files)}))

        for file in gpx_files:
            p = map_point.parse_gpx_file(file)
            p.user_id = u.uuid
            already_saved = dao_module.gpx_file_already_saved(session)(p)
            if not already_saved:
                logger.info("file hash not found in database.  Persisting",
                            logging_utils.wrap_props({"num_points": p.num_points(),
                                                      "file_name": p.name,
                                                      "hash": p.hash}))
                session.add(p)
                parse_files.append(p)
            else:
                logger.info("file hash already exists in db, not persisting",
                            logging_utils.wrap_props({"num_points": p.num_points(),
                                                      "file_name": p.name,
                                                      "hash": p.hash}))

        session.flush()




if __name__ == "__main__": main()




