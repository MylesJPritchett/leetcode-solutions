# Write your MySQL query statement below
select a.Name as Employee 
from Employee as A, Employee as b
where a.managerId = b.ID
and a.salary > b.salary