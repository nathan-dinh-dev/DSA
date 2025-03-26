# Write your MySQL query statement below
select name from (
    select e1.name, count(*) as numberReports
    from employee e1 INNER JOIN employee e2
    ON e1.id = e2.managerID
    group by e1.id
    ) as sub
where numberReports >= 5