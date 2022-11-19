INSERT INTO buildings (name)
VALUES ('COB'),
       ('PH1'),
       ('ECS'),
       ('KIN'),
       ('PSY'),
       ('DESN');

INSERT INTO rooms (building_name, room_number)
VALUES ('COB', 30),
       ('COB', 140),
       ('PH1', 402),
       ('DESN', 105),
       ('KIN', 213),
       ('PSY', 309);

INSERT INTO door_names (name)
VALUES ('Zuko'),
       ('Appa'),
       ('Aang'),
       ('Sokka'),
       ('Momo'),
       ('Ozai'),
       ('Front'),
       ('Back');

INSERT INTO doors (building_name, room_number, door_name)
VALUES ('COB', 30, 'Aang'),
       ('COB', 140, 'Sokka'),
       ('PH1', 402, 'Momo'),
       ('DESN', 105, 'Ozai'),
       ('KIN', 213, 'Front'),
       ('PSY', 309, 'Back');


INSERT INTO hooks (hook_number)
VALUES (1024),
       (1025),
       (1026),
       (1027),
       (1028),
       (1029);

INSERT INTO keys (hook_number)
VALUES (1024),
       (1025), (1025),
       (1026),
       (1027),
       (1028),
       (1029), (1029), (1029);

INSERT INTO employees (full_name)
VALUES ('Jimmy Johnson'),
       ('Michael Scott'),
       ('Pam Beasly'),
       ('Jim Halpert'),
       ('Ryan Reynolds'),
       ('Zendaya');

INSERT INTO hook_door_opening (hook_number, building_name, room_number, door_name)
VALUES (1024, 'COB', 30, 'Aang'),
       (1024, 'COB', 140, 'Sokka'),
       (1025, 'PSY', 309, 'Back'),
       (1026, 'PH1', 402, 'Momo'),
       (1027, 'DESN', 105, 'Ozai'),
       (1028, 'KIN', 213, 'Front'),
       (1029, 'PSY', 309, 'Back');

INSERT INTO room_requests (request_time, employee_id, building_name, room_number)
VALUES ('2022-11-19', 1, 'COB', 140),
       ('2022-10-19', 6, 'PH1', 402),
       ('2022-09-19', 4, 'DESN', 105),
       ('2022-08-19', 2, 'PSY', 309);
