import uuid
import json
import points.utils


class Payload(object):
    data = None
    sender = None
    id = None
    sent_at = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if self.id is None:
            self.id = str(uuid.uuid4())

        if self.sender is None:
            self.sender = "NOT_SPECIFIED"

        if self.sent_at is not None:
            self.sent_at = points.utils.string_to_datetime(self.sent_at)

    def to_payload(self) -> bytearray:
        now = points.utils.now()
        now = points.utils.datetime_to_string(now)

        payload = {
            "data": self.data,
            "sent_at": now,
            "id": self.id,
            "sender": self.sender,
        }

        ret = json.dumps(payload)
        return ret

    @staticmethod
    def from_bytes(bytes_arg: bytearray):
        d = json.loads(bytes_arg)
        p = Payload(**d)
        return p





