import os
import points.logging_utils as logging_utils
import points.pg.config as dao_config
import points.pg.dao as dao_module

logging_utils.init()
logger = logging_utils.create_logger("gpx_file_info")

def main():
    logger.info("fart")
    dao = dao_module.Dao.create_dao(dao_config.Config.from_env(os.environ))

    with dao.session_scope() as dao_session:
        all_files = dao_module.get_all_gpx_files(dao_session)()
        all_files.sort(key=lambda x: x.name)
        for i, gpx_file in enumerate(all_files):
            logger.info("gpx_file",
                        extra=logging_utils.wrap_props({"i": i,
                                                        "id": gpx_file.id,
                                                        "name": gpx_file.name,
                                                        "points_count": len(gpx_file.points)}))


if __name__ == "__main__": main()

