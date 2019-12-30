#!/usr/bin/env bash


python3 -m unittest test/model/test_datetime.py
python3 -m unittest test/model/point_test.py
python3 -m unittest test/model/point_set_test.py
python3 -m unittest test/model/map_point_test.py
python3 -m unittest test/utils_test.py

python3 -m unittest test/pg/test_config.py

export DATA_FILE=test/data/formated.gpx
python3 -m unittest test/gpx/xmltodict_test.py




