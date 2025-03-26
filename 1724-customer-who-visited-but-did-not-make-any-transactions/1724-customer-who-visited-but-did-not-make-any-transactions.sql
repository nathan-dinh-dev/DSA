# Write your MySQL query statement below
select v.customer_id, COUNT(v.visit_id) as count_no_trans
from visits v LEFT JOIN transactions t on v.visit_id = t.visit_id
WHERE t.transaction_id is null
GROUP BY v.customer_id