# https://leetcode.com/problems/article-views-i/submissions/?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below

SELECT DISTINCT(AUTHOR_ID) as ID
FROM VIEWS
WHERE VIEWER_ID = AUTHOR_ID
ORDER BY ID ASC;
