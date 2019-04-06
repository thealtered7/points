import points.model.point as point
import points.model.point_set as point_set
import psycopg2 as pg
import psycopg2.extensions as pg_extensions
import points.model.utils as utils
import sys
import random
import points.pg.config as pg_config
import os


class Dao(object):
    def __init__(self, session: pg_extensions.connection):
        self.__session = session

    def save_point_set(self, ps: point_set.PointSet):
        sql = "insert into point_set (name, created) values (%s, %s) returning id;"
        cursor = self.__session.cursor()

        try:
            cursor.execute(sql, (ps.name, ps.created))
            result_array = cursor.fetchone()
            id = result_array[0]
            ps.id = id

            ps.points = [p.set_point_set_id(id) for p in ps.points]
            ps.points = self.save_points(ps.points)
            self.__session.commit()

            return ps
        finally:
            cursor.close()

    def get_point_set_by_id(self, id: int):
        sql = "select id, name, created from point_set where id = %s"
        cursor = self.__session.cursor()
        try:
            cursor.execute(sql, (id,))
            result_set = cursor.fetchone()
            ps = point_set.PointSet()
            ps.id = result_set[0]
            ps.name = result_set[1]
            ps.created = result_set[2]
            ps.points = self.get_points_by_point_set_id(id)
            return ps
        finally:
            cursor.close()

    def save_points(self, point_list):
        sql = "insert into point (x, y, z, point_set_id) values (%s, %s, %s, %s) returning id;"
        cursor = self.__session.cursor()
        try:
            for p in point_list:
                cursor.execute(sql, (p.x, p.y, p.z, p.point_set_id))
                result_set = cursor.fetchone()
                p.id = result_set[0]

            self.__session.commit()
            return point_list
        finally:
            cursor.close()

    def get_points_by_point_set_id(self, id):
        sql = "select id, x, y, z, point_set_id from point where point_set_id = %s"
        cursor = self.__session.cursor()
        try:
            point_list = []
            cursor.execute(sql, (id,))
            results = cursor.fetchone()
            while results:
                p = point.Point()
                p.id = results[0]
                p.x = results[1]
                p.y = results[2]
                p.z = results[3]
                p.point_set_id = results[4]
                point_list.append(p)
                results = cursor.fetchone()

            return point_list
        finally:
            cursor.close()

def create_random_points(num_points, scale=100):
    point_list = []
    for i in range(num_points):
        p = point.Point()
        p.x = random.random() * scale
        p.y = random.random() * scale
        p.z = random.random() * scale
        point_list.append(p)

    return point_list

def main():
    config = pg_config.Config.from_env(os.environ)
    session = pg.connect("host={host} user={username} password={password} dbname={database}".format_map({"host": config.host,
                                                                                                         "username": config.username,
                                                                                                         "password": config.password,
                                                                                                         "database": config.database}))
    dao = Dao(session)

    ps = point_set.PointSet()
    ps.name = "Test Point Set"
    ps.created = utils.now()
    point_list = create_random_points(100, 100)
    ps.points = point_list

    try:
        ps = dao.save_point_set(ps)
    except Exception as e:
        sys.stderr.write("error saving point_set: {}\n".format(e,))
        os.exit(1)

    print(str(ps))

    try:
        ps = dao.get_point_set_by_id(ps.id)
    except Exception as e:
        sys.stderr.write("error getting point_set of id = {}: {}\n".format(ps.id, e))
        os.exit(1)

    print(str(ps))

    
if __name__ == "__main__":
    main()

