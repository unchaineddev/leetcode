# https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier
# Write your MySQL query statement below

SELECT euni.unique_id, e.name
FROM Employees as e
LEFT JOIN EmployeeUNI euni ON e.id = euni.id;
