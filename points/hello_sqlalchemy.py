import points.pg.dao as dao_module
import points.pg.config as dao_config
import os
import points.model.point as point
import points.model.point_set as point_set
import points.model.utils as utils
import random

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
    config = dao_config.Config.from_env(os.environ)
    dao = dao_module.create_dao(config)

    ps = point_set.PointSet()
    ps.points = create_random_points(10, 10)
    ps.created = utils.now()
    ps.name = "Hello SQLAlchemy"

    ps = dao.save_or_update_point_set(ps)
    ps = dao.get_point_set_by_id(ps.id)
    print(utils.to_json(ps))



if __name__ == "__main__":
    main()