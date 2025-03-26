# Write your MySQL query statement below
select u.unique_id, e.name from employees e LEFT JOIN employeeUNI u on e.id = u.id