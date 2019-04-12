from sqlalchemy.ext.declarative import declarative_base


__base = declarative_base()

def get_base():
    return __base

