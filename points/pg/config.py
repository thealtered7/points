import os

DefaultPort = "5432"

def get_development_env():
    environment = {
        "PGHOST": "localhost",
        "PGUSER": "postgres",
        "PGPASSWORD": "fart",
        "PGDATABASE": "points",
        "PGPORT": DefaultPort
    }
    return environment


class Config(object):

    def __init__(self):
        self.host = ""
        self.database = ""
        self.username = ""
        self.password = ""
        self.port = ""

    def from_env(env=os.environ):
        c = Config()
        c.host = env["PGHOST"]
        c.database = env["PGDATABASE"]
        c.username = env["PGUSER"]
        c.password = env["PGPASSWORD"]
        c.port = env["PGPORT"]
        if c.port is None or c.port == "":
            c.port = DefaultPort

        return c

    def connect_string(self):
        ret = "postgresql://{username}:{password}@{host}:{port}/{database}".format_map(self.__dict__)
        return ret


