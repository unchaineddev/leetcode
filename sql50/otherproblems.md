181. Employees Earning More Than Their Managers

#### https://leetcode.com/problems/employees-earning-more-than-their-managers/description/

<!-- # Write your MySQL query statement below -->
```sql
SELECT e1.name as Employee
from employee e1
inner join employee e2 on e2.id = e1.managerId
where e1.salary > e2.salary 
```