import typing


class Config(object):
    url = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @staticmethod
    def config_from_env(env: typing.Dict):
        url = env["NATS_SERVERS"]
        return Config(url=url)


