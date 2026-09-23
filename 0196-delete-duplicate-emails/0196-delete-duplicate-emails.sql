# Write your MySQL query statement below
DELETE Person1
FROM Person AS Person1
JOIN Person AS Person2
ON Person1.email = Person2.email
WHERE Person1.id > Person2.id;