# Write your MySQL query statement below
SELECT Employee.name AS Employee
FROM Employee
JOIN Employee AS manager
ON Employee.managerid = manager.id
WHERE Employee.salary > manager.salary;