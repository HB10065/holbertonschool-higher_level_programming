#!/usr/bin/python3
'''
Module Doc
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]

    db_url = (
        f'mysql+mysqldb://{mysql_user}:{mysql_pass}'
        f'@localhost:3306/{db_name}'
    )

    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')

    session.close()
