SELECT * 
FROM STUDENT 
WHERE Undergrad = TRUE;

SELECT S.FirstName, S.LastName, C.Title, T.Grade
FROM STUDENT S
JOIN TAKE T ON S.Student# = T.Student#
JOIN COURSE C ON T.Course# = C.Course#
WHERE S.Student# = 1;

SELECT Course#
FROM COURSE
WHERE InstName = 'Dr. Johnson';

SELECT S.Student#, S.FirstName, S.LastName, T.Grade
FROM STUDENT S
JOIN TAKE T ON S.Student# = T.Student#
WHERE T.Course# = 103;

SELECT S.Student#, S.FirstName, S.LastName, C.Title, T.Grade
FROM STUDENT S
JOIN TAKE T ON S.Student# = T.Student#
JOIN COURSE C ON T.Course# = C.Course#
WHERE T.Grade = 'A';

SELECT C.Title, AVG(CASE 
                     WHEN T.Grade = 'A' THEN 4 
                     WHEN T.Grade = 'B' THEN 3 
                     WHEN T.Grade = 'C' THEN 2 
                     WHEN T.Grade = 'D' THEN 1 
                     ELSE 0 
                   END) AS AverageGrade
FROM TAKE T
JOIN COURSE C ON T.Course# = C.Course#
WHERE C.Course# = 101
GROUP BY C.Title;

SELECT C.Title, COUNT(T.Student#) AS EnrolledStudents
FROM COURSE C
JOIN TAKE T ON C.Course# = T.Course#
GROUP BY C.Course#
HAVING COUNT(T.Student#) > 1;

SELECT C.Course#, C.Title, C.CrHour, I.InstName, I.InstOffice, I.Rank
FROM COURSE C
JOIN INSTRUCTOR I ON C.InstName = I.InstName;

SELECT S.Student#, S.FirstName, S.LastName, C.Title
FROM STUDENT S
JOIN TAKE T ON S.Student# = T.Student#
JOIN COURSE C ON T.Course# = C.Course#
WHERE C.InstName = 'Dr. Lee';

SELECT S.Student#, S.FirstName, S.LastName, C.Title, T.Grade
FROM STUDENT S
JOIN TAKE T ON S.Student# = T.Student#
JOIN COURSE C ON T.Course# = C.Course#
WHERE S.City = 'Los Angeles';