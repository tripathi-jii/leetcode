# Write your MySQL query statement below
SELECT Courses.class
FROM Courses
GROUP BY Courses.class
HAVING COUNT(Courses.student) >= 5;