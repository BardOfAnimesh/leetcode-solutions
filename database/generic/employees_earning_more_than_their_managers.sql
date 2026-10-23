-- ======================================
-- LeetCode Problem: employees earning more than their managers
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/employees-earning-more-than-their-managers/
-- Synced by: LinkCode
-- Date: 10/23/2026, 12:27:08 PM
-- ======================================


# Write your MySQL query statement below

select e.name as Employee from Employee as e join Employee as m on m.id=e.managerId
where e.salary>m.salary;