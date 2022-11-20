INSERT INTO buildings (name)
VALUES ('COB'),
       ('PH1'),
       ('ECS'),
       ('KIN'),
       ('PSY'),
       ('DESN');

INSERT INTO employees (full_name)
VALUES ('Jimmy Johnson'),
       ('Michael Scott'),
       ('Pam Beasly'),
       ('Jim Halpert'),
       ('Ryan Reynolds'),
       ('Zendaya');

INSERT INTO rooms (building_name, room_number)
VALUES ('COB', 30),
       ('COB', 23),
       ('PH1', 402),
       ('DESN', 105),
       ('KIN', 213),
       ('PSY', 309);

INSERT INTO door_names (name)
VALUES ('Front'),
       ('Back'),
       ('East'),
       ('West'),
       ('North'),
       ('South');

INSERT INTO doors (room_number, building_name, door_name)
VALUES (30, 'COB', 'Front'),
       (30, 'COB', 'Back'),
       (23, 'COB', 'Front'),
       (23, 'COB', 'Back'),
       (402, 'PH1', 'East'),
       (105, 'DESN', 'North'),
       (105, 'DESN', 'South'),
       (213, 'KIN', 'Front'),
       (309, 'PSY', 'East'),
       (309, 'PSY', 'West');

INSERT INTO hooks (hook_number)
VALUES (1),
       (2),
       (3),
       (4),
       (5),
       (6);

INSERT INTO hook_door_opening (hook_number, building_name, room_number, door_name)
VALUES (1,'COB', 30, 'Front'),
       (1,'COB', 30, 'Back'),
       (2,'COB', 30, 'Front'),
       (2,'COB', 23, 'Front'),
       (2,'COB', 23, 'Back'),
       (3, 'PH1', 402, 'East'),
       (4, 'DESN', 105, 'North'),
       (4, 'DESN', 105, 'South'),
       (5, 'KIN', 213, 'Front'),
       (6, 'PSY', 309, 'East'),
       (6, 'PSY', 309, 'West');

INSERT INTO keys (hook_number)
VALUES (1),
       (2),
       (2),
       (3),
       (4),
       (5),
       (5),
       (6);

INSERT INTO room_requests (request_time, employee_id, building_name, room_number)
VALUES (NOW(), 1, 'COB', 23),
       (NOW(), 2, 'COB', 23),
       (NOW(), 3, 'KIN', 213),
       (NOW(), 4, 'DESN', 105),
       (NOW(), 5, 'KIN', 213),
       (NOW(), 4, 'PSY', 309);

INSERT INTO key_issue (request_id, hook_number, key_number, start_time)
VALUES (1, 1, 1, NOW()),
       (2, 2, 2, NOW()),
       (3, 5, 6, NOW()),
       (4, 4, 5, NOW()),
       (5, 5, 7, NOW()),
       (6, 6, 8, NOW());

INSERT INTO key_issue_return (issue_number, return_date)
VALUES (1, NOW()),
       (2, NOW());

INSERT INTO key_issue_loss (issue_number, loss_date)
VALUES (3, NOW()),
       (4, NOW());





