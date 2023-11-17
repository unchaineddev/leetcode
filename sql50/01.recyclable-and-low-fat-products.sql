-- https://leetcode.com/problems/recyclable-and-low-fat-products/?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below

SELECT PRODUCT_ID
FROM PRODUCTS
WHERE LOW_FATS = 'Y' AND recyclable = 'Y';