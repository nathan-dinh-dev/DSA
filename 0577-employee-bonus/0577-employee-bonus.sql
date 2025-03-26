# Write your MySQL query statement below
SELECT e.name, b.bonus from employee e LEFT JOIN bonus b
ON e.empID = b.empID
WHERE b.bonus < 1000 or b.bonus is NULL