# Write your MySQL query statement below
SELECT Customer.name
FROM Customer
WHERE Customer.referee_id != 2 OR Customer.referee_id IS NULL;