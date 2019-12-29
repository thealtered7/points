import os
from typing import List

import pynats

import points.logging_utils as logging_utils
import points.model.map_point as map_point
import points.nats.payload as nats_payload
import points.nats.constructor as nats_constructor
import points.pg.config as dao_config
import points.pg.dao as dao_module

logging_utils.init()
logger = logging_utils.create_logger("pg_pull_nats_push")


def publish_gpx_files(client: pynats.NATSClient, files: List[map_point.GpxFile]):
    publisher_name = "gpx_files.gpx_file"
    for i, f in enumerate(files):
        logger.info("publishing file",
                    extra=logging_utils.wrap_props({"file_name": f.name,
                                                    "file_number": i}))

        payload = nats_payload.Payload(sender="pg_pull_nats_push", data={"file_id": f.id})
        payload_bytes = payload.to_payload()
        publish_name = publisher_name
        client.publish(subject=publish_name, payload=payload_bytes)


def main():
    env = os.environ
    config = dao_config.Config.from_env(env)
    dao = dao_module.create_dao(config)
    nats_config = nats_constructor.Config.config_from_env(env)

    logger.info("nats_url", extra=logging_utils.wrap_props({"nats_url": nats_config.url}))
    with pynats.NATSClient(url=nats_config.url) as nats_client:
        with dao.session_scope() as session:
            logger.info("getting all gpx files from postgres")
            all_gpx_files = dao_module.get_all_gpx_files(session)()
            logger.info("gpx files acquired",
                        extra=logging_utils.wrap_props({
                            "count": len(all_gpx_files),
                            "file_names": [x.name for x in all_gpx_files]
                        }))
            publish_gpx_files(nats_client, all_gpx_files)





if __name__ == "__main__":
    main()

