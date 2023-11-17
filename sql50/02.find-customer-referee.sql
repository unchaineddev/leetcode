-- https://leetcode.com/problems/find-customer-referee/?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below

SELECT NAME
FROM CUSTOMER
WHERE REFEREE_ID <> 2 or REFEREE_ID is NULL;

