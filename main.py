from db_connection import Session, engine
# orm_base defines the Base class on which we build all of our Python classes and in so doing,
# stipulates that the schema that we're using is 'demo'.  Once that's established, any class
# that uses Base as its supertype will show up in the postgres.demo schema.
import logging

from orm_base import metadata
from Building import Building
from Room import Room
from Door import Door
from DoorName import DoorName
from Hook import Hook
from Key import Key
from Employee import Employee

ECS_building = Building('ECS')
room1 = Room(ECS_building, 101)
front_door = DoorName("Front")
ECS101Front = Door(room1, front_door)
hook1 = Hook()
hook1key1 = Key(hook1)
hook1key2 = Key(hook1)
e1 = Employee('James Xiao')
e2 = Employee('Ke Zhong')

if __name__ == '__main__':
    logging.basicConfig()
    # use the logging factory to create our first logger.
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    # use the logging factory to create our second logger.
    logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)

    # metadata.drop_all(bind=engine)
    metadata.create_all(bind=engine)

    with Session() as sess:
        sess.begin()
        sess.add(ECS_building)
        sess.add(room1)
        sess.add(front_door)
        sess.add(ECS101Front)
        sess.add(hook1)
        sess.add(hook1key1)
        hook1.open_door(ECS101Front)

        # sess.add(e1)
        sess.add(e2)
        # employee 1 requests room 1 and given hook1key1
        rr1 = e1.request_room(room1)
        ki1 = rr1.issue_key(hook1key1)
        # employee 2 requests room 1 and given hook1key2
        rr2 = e2.request_room(room1)
        ki2 = rr2.issue_key(hook1key2)
        sess.commit()
        # employee 1 returns key
        ki1.return_key()
        # employee 2 loses key
        ki2.loss_key()
        # commit the changes
        sess.commit()

    print("Exiting normally.")
