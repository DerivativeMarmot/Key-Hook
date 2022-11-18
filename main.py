from db_connection import Session, engine
# orm_base defines the Base class on which we build all of our Python classes and in so doing,
# stipulates that the schema that we're using is 'demo'.  Once that's established, any class
# that uses Base as its supertype will show up in the postgres.demo schema.
import logging

from orm_base import metadata
from Building import Building
from Room import Room
from RoomRequest import RoomRequest
from Door import Door
from DoorName import DoorName
from KeyIssue import KeyIssue
from Hook import Hook
from Key import Key
from Employee import Employee
from HookDoorOpening import HookDoorOpening

# ECS_building = Building('ECS')
# room1 = Room(ECS_building, 101)
# front_door = DoorName("Front")
# ECS101Front = Door(room1, front_door)
# hook1 = Hook()
# hook1key1 = Key(hook1)
# hook1key2 = Key(hook1)
# e1 = Employee('James Xiao')
# e2 = Employee('Ke Zhong')

# add statements
# sess.add(ECS_building)
# sess.add(room1)
# sess.add(front_door)
# sess.add(ECS101Front)
# sess.add(hook1)
# sess.add(hook1key1)
# hook1.open_door(ECS101Front)
#
# # sess.add(e1)
# sess.add(e2)
# # employee 1 requests room 1 and given hook1key1
# rr1 = e1.request_room(room1)
# ki1 = rr1.issue_key(hook1key1)
# # employee 2 requests room 1 and given hook1key2
# rr2 = e2.request_room(room1)
# ki2 = rr2.issue_key(hook1key2)
# sess.commit()
# # employee 1 returns key
# ki1.return_key()
# # employee 2 loses key
# ki2.loss_key()
# # commit the changes


if __name__ == '__main__':
    # logging.basicConfig()
    # # use the logging factory to create our first logger.
    # logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    # # use the logging factory to create our second logger.
    # logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)

    # metadata.drop_all(bind=engine)
    # metadata.create_all(bind=engine)

    with Session() as sess:
        sess.begin()

    x = -1
    while x != 0:
        # menu that prints out the different actions the user can do
        print("Menu options:\n1.\tCreate a key\n2.\tEmployee Room Request\n3.\tIssue a key\n4.\tLosing a key\n5.\tRooms "
              "employee can enter\n6.\t"
              "Delete Key\n7.\tDelete Employee\n8.\tAdd Door to a hook\n9.\tUpdate Access Request\n"
              "10.\tEmployees that can enter a room\n0.\tExit")
        x = int(input('> '))

        if x == 1:  # create a new key
            print("Which hook would you like to apply to this key?")
            hk: [Hook] = sess.query(Hook).all()  # query of the different hooks
            hk_display: [Hook] = sess.query(Hook.hook_number).all()  # query of the hook numbers
            
            print("hook number")
            for index, row in enumerate(hk_display):  # for loop that prints out a list of the existing hook numbers
                print(index, ":", row)
                
            new_key = Key(hk[int(input())])  # creates a new key object to add into the table / add a new key to an existing hook
            sess.add(new_key)  # adds key into table
            print("Key has been created")
            sess.commit()

        elif x == 2:  # Key Request for an Employee
            emp: [Employee] = sess.query(Employee).all()
            emp_display: [Employee] = sess.query(Employee.id, Employee.full_name).all()
            
            print("Which employee wants a room request?")
            for index, row in enumerate(emp_display):
                print(index, ":", row)
            response_1 = int(input())
            
            print("Which room does the employee want access to?")
            rm: [Room] = sess.query(Room).all()
            rm_display: [Room] = sess.query(Room.room_number, Room.building_name).all()
            option = 0
            for row in rm_display:
                print(option, ":", row)
                option += 1
            response_2 = int(input())
            rmReq = emp[response_1].request_room(rm[response_2])
            print("Employee has requested for a room")
            sess.commit()

        elif x == 3:
            print("Which room request do you want to issue to?")
            rmReq: [RoomRequest] = sess.query(RoomRequest).all()
            option = 0
            for row in rmReq:
                print(option, ":", row)
                option += 1
            response = int(input())
            # this is without checking if room request is valid
            # needs to be filled with a key, not sure how to access certain keys though
            kyIss = rmReq[response].issue_key() # waiting for initial data

        elif x == 4:
            print("Which key has been lost?")
            kyIss: [KeyIssue] = sess.query(KeyIssue).all()
            kyIss_display: [KeyIssue] = sess.query(KeyIssue.issue_number, KeyIssue.key_number,
                                                   KeyIssue.hook_number).all()
            option = 0
            for row in kyIss_display:
                print(option, ":", row)
                option += 1
            response = int(input())
            kyIss[response].loss_key()
            print("Key has been lost...")

        elif x == 5:
            print("Which employee do you want to view?")
            emp: [Employee] = sess.query(Employee).all()
            emp_display: [Employee] = sess.query(Employee.id, Employee.full_name).all()
            option = 0
            print("(Employee ID, Employee Name)")
            for row in emp_display:
                print(option, ":", row)
                option += 1
            response = int(input())
            print("These are the rooms this employee can enter:\n")
            # query searching employee and their key

        elif x == 6:
            print("Which key would you like to delete?")
            k: [Key] = sess.query(Key).all()
            k_display: [Key] = sess.query(Key.key_number, Key.hook_number).all()
            option = 0
            print("(key number, hook number)")
            for row in k_display:
                print(option, ":", row)
                option += 1
            response = int(input())
            print("Deleting Key...")
            sess.delete(k[response])
            sess.commit()

        elif x == 7:
            print("Which employee would you like to delete?")
            emp: [Employee] = sess.query(Employee).all()
            emp_display: [Employee] = sess.query(Employee.id, Employee.full_name).all()
            option = 0
            print("(Employee ID, Employee Name)")
            for row in emp_display:
                print(option, ":", row)
                option += 1
            response = int(input())
            print("Deleting Employee...")
            sess.delete(emp[response])
            sess.commit()

        elif x == 8:
            print("Which hook do you want to access?")
            hk: [Hook] = sess.query(Hook).all()
            hk_display: [Hook] = sess.query(Hook.hook_number).all()
            option = 0
            print("hook number")
            for row in hk_display:
                print(option, ":", row)
                option += 1
            response_1 = int(input())
            print("Which door do you want to add to this hook?")
            dr: [Door] = sess.query(Door).all()
            dr_display: [Door] = sess.query(Door.building_name, Door.room_number, Door.door_name)
            option = 0
            for row in dr_display:
                print(option, ":", row)
                option += 1
            response_2 = int(input())
            print("Adding door to hook")
            hk[response_1].open_door(dr[response_2])
            sess.commit()

        elif x == 9:
            print("Updating access request")

        elif x == 10:
            print("Which room would you want to oversee?")
            hkOp: [HookDoorOpening] = sess.query(HookDoorOpening).all()
            hkOp_display: [HookDoorOpening] = sess.query(HookDoorOpening.room_number,
                                                         HookDoorOpening.building_name).all()
            option = 0
            for row in hkOp_display:
                print(option, ":", row)
                option += 1
            response = int(input())
            print("These are the rooms this employee can access:")
            kyIss: [KeyIssue] = sess.query(KeyIssue.request_id).filter_by(hook_number=hkOp[response].hook_number)
            
