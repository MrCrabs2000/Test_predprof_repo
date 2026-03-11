from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.classes import table_base

Session = None

def init_database():
    global Session
    if Session:
        return

    engine = create_engine('sqlite:///db/database.db', echo = False)
    Session = sessionmaker(bind=engine)
    table_base.metadata.create_all(engine)


def create_session():
    global Session
    return Session