-- ======================================
-- LeetCode Problem: department top three salaries
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/department-top-three-salaries/
-- Synced by: LinkCode
-- Date: 11/18/2026, 10:38:22 PM
-- ======================================


# Write your MySQL query statement below
with ranked_emp as (
    select name,
    id, departmentId,salary,
    Dense_rank() over(partition by departmentId
    order by salary DESC  
    )
    As rnked
    from Employee
)

Select d.name as Department,r.name as Employee,r.salary as Salary 
from ranked_emp as r join Department as d on r.departmentId=d.id
where rnked<=3 order by r.salary Desc