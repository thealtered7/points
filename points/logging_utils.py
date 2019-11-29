import sys
import logging
import json_logging


def init():
    json_logging.ENABLE_JSON_LOGGING = True
    json_logging.init_non_web()


def create_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.setLevel(logging.INFO)
    return logger


def wrap_props(d: dict) -> dict:
    return {"props": d}

