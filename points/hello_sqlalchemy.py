import points.pg.dao as dao_module
import points.pg.config as dao_config
import os
import points.model.json as json

def main():
    config = dao_config.Config.from_env(os.environ)
    dao = dao_module.Dao.create_dao(config)

    point_set = dao.get_point_set_by_id(23)
    print(json.to_json(point_set))



if __name__ == "__main__":
    main()