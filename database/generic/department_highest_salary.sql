-- ======================================
-- LeetCode Problem: department highest salary
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/department-highest-salary/
-- Synced by: LinkCode
-- Date: 11/14/2026, 12:41:10 AM
-- ======================================


# Write your MySQL query statement below
select  d.name as Department, e.name as Employee,e.salary as Salary from Employee as e left join Department as d on d.id=e.departmentId 
WHERE (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
)