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
from HookDoorOpening import HookDoorOpening
from Key import Key
from Employee import Employee
from RoomRequest import RoomRequest
from KeyIssue import KeyIssue

ECS_building = Building('ECS')
room1 = Room(ECS_building, 101)
front_door = DoorName("Front")
ECS101Front = Door(room1, front_door)
hook1 = Hook(1)
hook1key1 = Key(hook1, 1)
print('key number shism',hook1key1.key_number)
opening1 = HookDoorOpening(hook1, ECS101Front)
e1 = Employee('James Xiao')
# somehow this would add another room request to the table even without sess.add(rr)
# rr = RoomRequest(e1, room1)

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
        sess.add(opening1)

        sess.add(e1)
        rr = e1.request_room(room1)
        rr.issue_key(hook1key1)
        # ki = KeyIssue(rr, hook1key1)
        # sess.add(ki)

        # commit the changes
        sess.commit()


    print("Exiting normally.")
