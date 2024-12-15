CREATE TABLE STUDENT (
    Student# INT PRIMARY KEY,
    LastName VARCHAR(50),
    FirstName VARCHAR(50),
    Address VARCHAR(100),
    City VARCHAR(50),
    State VARCHAR(50),
    Zip VARCHAR(10),
    Enroll_Date DATE,
    Undergrad BOOLEAN
);

CREATE TABLE COURSE (
    Course# INT PRIMARY KEY,
    Title VARCHAR(100),
    CrHour INT,
    InstName VARCHAR(50),
    FOREIGN KEY (InstName) REFERENCES INSTRUCTOR(InstName)
);

CREATE TABLE INSTRUCTOR (
    InstName VARCHAR(50) PRIMARY KEY,
    InstOffice VARCHAR(50),
    Rank VARCHAR(20)
);

CREATE TABLE TAKE (
    Student# INT,
    Course# INT,
    Grade CHAR(1),
    PRIMARY KEY (Student#, Course#),
    FOREIGN KEY (Student#) REFERENCES STUDENT(Student#),
    FOREIGN KEY (Course#) REFERENCES COURSE(Course#)
);