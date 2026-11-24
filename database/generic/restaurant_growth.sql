-- ======================================
-- LeetCode Problem: restaurant growth
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/restaurant-growth/
-- Synced by: LinkCode
-- Date: 11/25/2026, 12:50:14 AM
-- ======================================


# Write your MySQL query statement below
with daily as(
select visited_on, 
sum(amount) as roz_mount

from Customer Group by visited_on),

rolling as (
    select visited_on, 
sum(roz_mount)  over (
    order by visited_on
    rows between 6 preceding and current row ) as amount,
round(sum(roz_mount) over (
    order by visited_on
    rows between 6 preceding and current row )/7,2) as average_amount 
from daily 
)

select visited_on,amount,average_amount from rolling
where visited_on >= DATE_ADD((SELECT MIN(visited_on) FROM Customer), INTERVAL 6 DAY)
 order by visited_on