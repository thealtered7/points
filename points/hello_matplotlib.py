import points.pg.dao as dao_module
import points.pg.config as dao_config
import points.model.point_set as point_set
import os

import numpy as np
import matplotlib.pyplot as plt


def plot_point_set(point_set: point_set.PointSet):
    x = np.array([p.x for p in point_set.points])
    y = np.array([p.y for p in point_set.points])

    plt.scatter(x, y,  c="g", alpha=0.5, label="{} ({})".format(point_set.name, point_set.id))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(loc='upper left')
    plt.show()


def main():
    config = dao_config.Config.from_env(os.environ)
    dao = dao_module.Dao.create_dao(config)
    point_set = dao.get_point_set_by_id(35)
    point_set.points = sorted(point_set.points, key=lambda p: p.x)
    a = np.array([[x.x, x.y, x.z] for x in point_set.points])
    print(a)

    plot_point_set(point_set)


if __name__ == "__main__":
    main()