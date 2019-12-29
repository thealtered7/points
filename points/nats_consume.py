import os
import points.logging_utils as logging_utils
import points.pg.config as dao_config
import points.pg.dao as dao_module
import points.nats.constructor as nats_constructor
import asyncio
from nats.aio.client import Client as NatsClient

logging_utils.init()
logger = logging_utils.create_logger("nats_consume")


async def message_call_back(message):
    logger.info("message received", extra=logging_utils.wrap_props({"message": message}))

async def run_loop(loop, nats_config: nats_constructor.Config, dao: dao_module.Dao):
    topic = "gpx_files.gpx_file"
    nats_client = NatsClient()

    logger.info("connecting", extra=logging_utils.wrap_props({"url": nats_config.url}))
    await nats_client.connect(nats_config.url, loop=loop)
    logger.info("subscribing...")
    await nats_client.subscribe(topic, cb=message_call_back)
    logger.info("draining")
    await nats_client.drain()


def main():
    env = os.environ
    nats_loop = asyncio.get_event_loop()

    nats_config = nats_constructor.Config.config_from_env(env)
    dao_conf = dao_config.Config.from_env(env)
    dao = dao_module.create_dao(dao_conf)

    nats_loop.run_until_complete(run_loop(nats_loop, nats_config, dao))
    nats_loop.close()







if __name__ == "__main__":
    main()
