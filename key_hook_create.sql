-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-11-19 18:51:10.769

-- tables
-- Table: buildings
CREATE TABLE buildings (
    name varchar(200)  NOT NULL,
    CONSTRAINT buildings_pk PRIMARY KEY (name)
);

-- Table: door_names
CREATE TABLE door_names (
    name varchar(100)  NOT NULL,
    CONSTRAINT door_names_pk PRIMARY KEY (name)
);

-- Table: doors
CREATE TABLE doors (
    room_number int  NOT NULL,
    building_name varchar(200)  NOT NULL,
    door_name varchar(100)  NOT NULL,
    CONSTRAINT doors_pk PRIMARY KEY (room_number,building_name,door_name)
);

-- Table: employees
CREATE TABLE employees (
    id serial  NOT NULL,
    full_name varchar(200)  NOT NULL,
    CONSTRAINT employees_pk PRIMARY KEY (id)
);

-- Table: hook_door_opening
CREATE TABLE hook_door_opening (
    hook_number int  NOT NULL,
    building_name varchar(200)  NOT NULL,
    room_number int  NOT NULL,
    door_name varchar(100)  NOT NULL,
    CONSTRAINT hook_door_opening_pk PRIMARY KEY (hook_number,building_name,room_number,door_name)
);

-- Table: hooks
CREATE TABLE hooks (
    hook_number serial  NOT NULL,
    CONSTRAINT hooks_pk PRIMARY KEY (hook_number)
);

-- Table: key_issue
CREATE TABLE key_issue (
    issue_number serial  NOT NULL,
    request_id int  NOT NULL,
    hook_number int  NOT NULL,
    key_number int  NOT NULL,
    start_time date  NOT NULL,
    CONSTRAINT key_issue_pk PRIMARY KEY (issue_number)
);

-- Table: key_issue_loss
CREATE TABLE key_issue_loss (
    issue_number int  NOT NULL,
    loss_date date  NOT NULL,
    CONSTRAINT key_issue_loss_pk PRIMARY KEY (issue_number)
);

-- Table: key_issue_return
CREATE TABLE key_issue_return (
    issue_number int  NOT NULL,
    return_date date  NOT NULL,
    CONSTRAINT key_issue_return_pk PRIMARY KEY (issue_number)
);

-- Table: keys
CREATE TABLE keys (
    hook_number int  NOT NULL,
    key_number serial  NOT NULL,
    CONSTRAINT keys_pk PRIMARY KEY (hook_number,key_number)
);

-- Table: room_requests
CREATE TABLE room_requests (
    request_id serial  NOT NULL,
    request_time date  NOT NULL,
    employee_id int  NOT NULL,
    building_name varchar(200)  NOT NULL,
    room_number int  NOT NULL,
    CONSTRAINT room_requests_pk PRIMARY KEY (request_id)
);

-- Table: rooms
CREATE TABLE rooms (
    building_name varchar(200)  NOT NULL,
    room_number int  NOT NULL,
    CONSTRAINT rooms_pk PRIMARY KEY (room_number,building_name)
);

-- foreign keys
-- Reference: Table_9_hooks_fk_01 (table: hook_door_opening)
ALTER TABLE hook_door_opening ADD CONSTRAINT Table_9_hooks_fk_01
    FOREIGN KEY (hook_number)
    REFERENCES hooks (hook_number)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: doors_door_names_fk_01 (table: doors)
ALTER TABLE doors ADD CONSTRAINT doors_door_names_fk_01
    FOREIGN KEY (door_name)
    REFERENCES door_names (name)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: doors_rooms_fk_01 (table: doors)
ALTER TABLE doors ADD CONSTRAINT doors_rooms_fk_01
    FOREIGN KEY (room_number, building_name)
    REFERENCES rooms (room_number, building_name)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: hook_door_opening_doors_fk_01 (table: hook_door_opening)
ALTER TABLE hook_door_opening ADD CONSTRAINT hook_door_opening_doors_fk_01
    FOREIGN KEY (room_number, building_name, door_name)
    REFERENCES doors (room_number, building_name, door_name)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: key_issue_loss_key_issue_fk_01 (table: key_issue_loss)
ALTER TABLE key_issue_loss ADD CONSTRAINT key_issue_loss_key_issue_fk_01
    FOREIGN KEY (issue_number)
    REFERENCES key_issue (issue_number)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: key_issue_return_key_issue_fk_01 (table: key_issue_return)
ALTER TABLE key_issue_return ADD CONSTRAINT key_issue_return_key_issue_fk_01
    FOREIGN KEY (issue_number)
    REFERENCES key_issue (issue_number)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: key_issue_room_requests_fk_01 (table: key_issue)
ALTER TABLE key_issue ADD CONSTRAINT key_issue_room_requests_fk_01
    FOREIGN KEY (request_id)
    REFERENCES room_requests (request_id)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: key_requests_keys_fk_01 (table: key_issue)
ALTER TABLE key_issue ADD CONSTRAINT key_requests_keys_fk_01
    FOREIGN KEY (hook_number, key_number)
    REFERENCES keys (hook_number, key_number)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: keys_hooks (table: keys)
ALTER TABLE keys ADD CONSTRAINT keys_hooks
    FOREIGN KEY (hook_number)
    REFERENCES hooks (hook_number)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: room_requests_employees_fk_01 (table: room_requests)
ALTER TABLE room_requests ADD CONSTRAINT room_requests_employees_fk_01
    FOREIGN KEY (employee_id)
    REFERENCES employees (id)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: room_requests_rooms_fk_01 (table: room_requests)
ALTER TABLE room_requests ADD CONSTRAINT room_requests_rooms_fk_01
    FOREIGN KEY (room_number, building_name)
    REFERENCES rooms (room_number, building_name)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: rooms_buildings_fk_01 (table: rooms)
ALTER TABLE rooms ADD CONSTRAINT rooms_buildings_fk_01
    FOREIGN KEY (building_name)
    REFERENCES buildings (name)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- End of file.

