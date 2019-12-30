import unittest
import points.nats.payload as payload


class PayloadTest(unittest.TestCase):
    def test_constructor(self):
        p = payload.Payload(data="fart")
        self.assertEqual(p.data, "fart")
        self.assertIsNotNone(p.id)
        self.assertIsNotNone(p.sender)
        self.assertIsNone(p.sent_at)

        p = payload.Payload(data={"foo": "bar"}, id="fart", sender="some_service")
        self.assertEqual(p.data, {"foo": "bar"})
        self.assertEqual(p.id, "fart")
        self.assertEqual(p.sender, "some_service")
        self.assertIsNone(p.sent_at)

    def test_to_payload(self):
        p = payload.Payload(data={"foo": "bar"}, id="fart", sender="some_service")
        bytes_stuff = p.to_payload()
        self.assertTrue(type(bytes_stuff), bytes)

    def test_from_payload(self):
        p = payload.Payload(data={"foo": "bar"}, id="fart", sender="some_service")
        bytes_stuff = p.to_payload()
        p2 = payload.Payload.from_bytes(bytes_stuff)
        self.assertEqual(p.id, p2.id)
        self.assertEqual(p.sender, p2.sender)
        self.assertIsNotNone(p2.sent_at)
        self.assertEqual(p.data, p2.data)


