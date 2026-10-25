-- ======================================
-- LeetCode Problem: rising temperature
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/rising-temperature/
-- Synced by: LinkCode
-- Date: 10/25/2026, 5:53:42 PM
-- ======================================


# Write your MySQL query statement below
select t.id as Id from Weather as y join Weather as t on DATEDIFF(t.recordDate,y.recordDate)=1 where y.temperature<t.temperature;

