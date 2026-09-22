# Write your MySQL query statement below
SELECT Department.name AS Department, Employee.name AS Employee, Employee.salary AS Salary
FROM Employee
LEFT JOIN Department
ON Employee.departmentId = Department.id
WHERE 3 > (
    SELECT COUNT(DISTINCT salary)
    FROM Employee AS Employee2
    WHERE Employee2.departmentId = Employee.departmentId AND Employee2.salary > Employee.salary
);