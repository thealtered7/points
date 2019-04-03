import unittest
import points.pg.config as pg_config

class TestConfig(unittest.TestCase):
    environment = pg_config.get_development_env()

    def test_from_env(self):
        config = pg_config.Config.from_env(self.environment)
        self.assertEqual(config.password, "fart", "password should match")
        self.assertEqual(config.username, "postgres", "username should match")
        self.assertEqual(config.database, "points", "database should match")
        self.assertEqual(config.host, "localhost", "host should match")
        self.assertEqual(config.port, pg_config.DefaultPort, "port should match")

    def test_connect_string(self):
        config = pg_config.Config.from_env(self.environment)
        connect = config.connect_string()
        self.assertEqual("postgresql://postgres:fart@localhost:5432/points", connect, "connect string should match")
