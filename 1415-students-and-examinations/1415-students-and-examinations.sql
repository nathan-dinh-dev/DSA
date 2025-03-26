# Write your MySQL query statement below
select s.student_id, s.student_name, sub.subject_name, IFNULL(grouped.attended_exams, 0) as attended_exams
from students s CROSS JOIN subjects sub

LEFT JOIN (
    select student_id, subject_name, COUNT(*) AS attended_exams
    from examinations
    group by student_id, subject_name
) grouped
ON s.student_id = grouped.student_id and grouped.subject_name = sub.subject_name
ORDER BY s.student_id, sub.subject_name ASC 
