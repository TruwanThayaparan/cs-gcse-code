-- These are the most original Friend names ever

DROP TABLE iF EXISTS Friends;
CREATE TABLE Friends(ID INT, FriendName TEXT, Gender TEXT);

INSERT INTO Friends VALUES(1, 'Fake', 'M');
INSERT INTO Friends VALUES(2, 'Name', 'M');
INSERT INTO Friends VALUES(3, 'Not', 'F');
INSERT INTO Friends VALUES(4, 'Real', 'F');
INSERT INTO Friends VALUES(5, 'Ok', 'M');

UPDATE Friends
SET FriendName = 'Unreal', Gender = 'M'
WHERE ID = 4;

DELETE FROM Friends
WHERE ID = 2;

SELECT * FROM Friends;

