# Write your MySQL query statement below
SELECT Department.name AS Department, Employee.name AS Employee, Employee.salary AS Salary
FROM Employee
JOIN Department
ON Employee.departmentId = Department.id
WHERE Employee.salary = (
    SELECT MAX(Employee2.salary)
    FROM Employee AS Employee2
    WHERE Employee2.departmentId = Employee.departmentId
)