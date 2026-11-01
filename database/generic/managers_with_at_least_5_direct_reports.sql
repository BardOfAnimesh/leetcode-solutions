-- ======================================
-- LeetCode Problem: managers with at least 5 direct reports
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
-- Synced by: LinkCode
-- Date: 11/1/2026, 9:25:08 PM
-- ======================================


# Write your MySQL query statement below
select name from Employee where id in(select managerId from employee group by managerId having count(*)>=5)
