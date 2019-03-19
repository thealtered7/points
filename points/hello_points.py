import sys
import random

import points.model.point_set as ps
import points.model.point as p


def main():
    point_set = ps.PointSet()
    point_set.name = "My Point Set"
    point_set.id = 40
    point_set.created = ps.now()

    for i in range(0, 100):
        point = p.Point()
        point.point_set_id = point_set.id
        point.x = random.random()
        point.y = random.random()
        point.x = random.random()
        point_set.points.append(point)

    sys.stdout.write(str(point_set))
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
