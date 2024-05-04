-- https://leetcode.com/problems/employee-bonus/

-- Write your MySQL query statement below

SELECT e.name, b.bonus
from Employee e
LEFT JOIN bonus b ON e.empId = b.empId
where b.bonus < 1000 or b.bonus is null
