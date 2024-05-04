# Write your MySQL query statement below
-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

select m.name
from employee e
join employee m
where e.managerid=m.id
group by e.managerid
having count(*) >=5
