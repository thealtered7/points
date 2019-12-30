import points.model.base as base
import json as js
from sqlalchemy import Column, Integer, String

Base = base.get_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    uuid = Column(String, nullable=False, index=True)

    def __init__(self, **kwargs):
        Base.__init__(self)
        self.id = -1
        self.first_name = None
        self.last_name = None
        self.uuid = None

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __repr__(self):
        return ", ".join(["{}: {}".format(k, v) for k, v in self.__dict__.items()])

    def __str__(self):
        return self.__repr__()

    def to_json_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "uuid": self.uuid
        }

    @staticmethod
    def from_dict(data):
        return User(data)

    @staticmethod
    def from_json(arg):
        json_dict = js.loads(arg)
        return User(**json_dict)
