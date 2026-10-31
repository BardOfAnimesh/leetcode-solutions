-- ======================================
-- LeetCode Problem: queries quality and percentage
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/queries-quality-and-percentage/
-- Synced by: LinkCode
-- Date: 10/31/2026, 8:22:05 PM
-- ======================================


# Write your MySQL query statement below
select query_name,
round(avg(rating/position),2) as quality,
round(avg(case when rating<3 then 1 else 0 end)*100,2) as poor_query_percentage
from Queries group by query_name;
