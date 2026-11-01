-- ======================================
-- LeetCode Problem: managers with at least 5 direct reports
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
-- Synced by: LinkCode
-- Date: 11/1/2026, 9:57:12 PM
-- ======================================


# Write your MySQL query statement below
select e.name from Employee as e join Employee as m on e.id=m.managerId group by e.id having count(m.managerId)>=5;
