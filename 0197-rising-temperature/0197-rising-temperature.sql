# Write your MySQL query statement below
SELECT Weather.id
FROM Weather
JOIN Weather AS W1
ON DATEDIFF(Weather.recordDate, W1.recordDate) = 1
WHERE Weather.temperature > W1.temperature;