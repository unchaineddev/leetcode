# https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

# Write your MySQL query statement below

SELECT v.customer_id, COUNT(v.visit_id) as count_no_trans
FROM VISITS v 
LEFT JOIN TRANSACTIONS t ON v.visit_id = t.visit_id
where t.transaction_id is Null
GROUP BY v.customer_id; 
