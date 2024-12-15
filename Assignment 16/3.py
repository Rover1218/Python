INSERT INTO STUDENT (Student#, LastName, FirstName, Address, City, State, Zip, Enroll_Date, Undergrad)
VALUES 
(1, 'Smith', 'John', '123 Main St', 'Los Angeles', 'CA', '90001', '2020-08-15', TRUE),
(2, 'Doe', 'Jane', '456 Elm St', 'San Francisco', 'CA', '94102', '2019-09-10', FALSE),
(3, 'Brown', 'James', '789 Pine St', 'Seattle', 'WA', '98101', '2021-01-12', TRUE);

INSERT INTO INSTRUCTOR (InstName, InstOffice, Rank)
VALUES 
('Dr. Johnson', 'Room 101', 'Professor'),
('Dr. Lee', 'Room 202', 'Associate Professor'),
('Dr. Miller', 'Room 303', 'Assistant Professor');

INSERT INTO COURSE (Course#, Title, CrHour, InstName)
VALUES 
(101, 'Database Systems', 3, 'Dr. Johnson'),
(102, 'Operating Systems', 4, 'Dr. Lee'),
(103, 'Artificial Intelligence', 3, 'Dr. Miller');

INSERT INTO TAKE (Student#, Course#, Grade)
VALUES 
(1, 101, 'A'),
(1, 102, 'B'),
(2, 101, 'B'),
(2, 103, 'A'),
(3, 103, 'B'),
(3, 102, 'A');