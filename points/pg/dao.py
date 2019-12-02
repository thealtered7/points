import points.pg.config as config
from points.model.base import get_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.orm import eagerload_all
from points.model.point_set import PointSet
import points.model.map_point as map_point
import points.model.user as user
from contextlib import contextmanager
from typing import List

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

    @contextmanager
    def session_scope(self) -> Session:
        session = self.__session_maker()
        try:
            yield session
            session.commit()
            session.flush()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_point_set_by_id(self, id: int):
        with self.session_scope() as s:
            ret = s.query(PointSet).filter(PointSet.id == id).one()
            return ret

    def save_or_update_point_set(self, ps: PointSet):
        s = self.__session_maker()
        s.add(ps)
        s.commit()
        return ps

    def get_gpx_file_by_id(self, id: int):
        s = self.__session_maker()
        ret = s.query(map_point.GpxFile).filter(map_point.GpxFile.id == id).one()
        return ret

    def save_or_update_gpx_file(self, g: map_point.GpxFile):
        with self.session_scope() as s:
            s.add(g)
            s.commit()
            s.flush()
            s.expunge_all()

        return self.get_gpx_file_by_id(g.id)

    def get_user(self, **kwargs):
        id = kwargs["id"]
        with self.session_scope() as s:
            u = s.query(user.User).options(eagerload_all('*')).filter(user.User.id == id).one()
            s.expunge(u)
            return u


    def get_all_gpx_points(self):
        with self.session_scope() as s:
            ret = s.query(map_point.GpxPoint).options(eagerload_all('gpx_point.*')).all()
            return ret


def create_dao(c: config.Config) -> Dao:
    return Dao.create_dao(c)


def get_all_gpx_files(session):
    def f() -> List[map_point.GpxFile]:
        gpx_files = session.query(map_point.GpxFile).all()
        return gpx_files
    return f


def get_user(session):
    def f(**kwargs) -> user.User:
        id = kwargs["id"]
        u = session.query(user.User).options(eagerload_all('*')).filter(user.User.id == id).one()
        session.expunge(u)
        return u

    return f


def gpx_file_already_saved(session):
    def f(gpx_file: map_point.GpxFile) -> bool:
        result = session.query(map_point.GpxFile).filter(map_point.GpxFile.hash == gpx_file.hash).all()
        return len(result) > 0

    return f
