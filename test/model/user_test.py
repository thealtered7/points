import unittest
import points.model.user as user
import points.utils as utils


class MapPointTest(unittest.TestCase):
    def test_user_json(self):
        p = user.User(id=1,
                      first_name="Jeffrey",
                      last_name="Keene",
                      uuid=utils.create_uuid_str())

        json_data = utils.to_json(p)
        self.assertTrue(json_data is not None)
        user2 = user.User.from_json(json_data)
        self.assertEqual(p.id, user2.id)
        self.assertEqual(p.first_name, user2.first_name)
        self.assertEqual(p.last_name, user2.last_name)
        self.assertEqual(p.uuid, user2.uuid)

