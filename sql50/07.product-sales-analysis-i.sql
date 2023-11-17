
# https://leetcode.com/problems/product-sales-analysis-i/?envType=study-plan-v2&envId=top-sql-50
# Write your MySQL query statement below


SELECT p.product_name, s.year, s.price
FROM SALES s
JOIN product p ON p.product_id = s.product_id;
