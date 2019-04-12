import points.pg.config as config
from points.model.base import get_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from points.model.point_set import PointSet

def create_points_engine(c: config.Config):
    connection_string = c.connect_string()
    engine = create_engine(connection_string)
    return engine


class Dao(object):
    def __init__(self):
        self.__session_maker = None


    def create_dao(c: config.Config):
        dao = Dao()
        e = create_points_engine(c)
        session = sessionmaker()
        session.configure(bind=e)
        base = get_base()
        base.metadata.create_all(e)
        dao.__session_maker = session

        return dao

    def get_point_set_by_id(self, id: int):
        s = self.__session_maker()
        ret = s.query(PointSet).filter(PointSet.id == id).one()
        return ret

    def save_or_update_point_set(self, ps: PointSet):
        s = self.__session_maker()
        s.add(ps)
        s.commit()
        return ps
