-- ======================================
-- LeetCode Problem: consecutive numbers
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/consecutive-numbers/
-- Synced by: LinkCode
-- Date: 11/2/2026, 10:29:24 PM
-- ======================================


# Write your MySQL query statement below
with orderlogs as(
    select 
    num,
    lag(num,1) over (order by id) as next_num1,
    lag(num,2) over (order by id) as next_num2
    from logs
)

select distinct num as ConsecutiveNums from orderlogs where num=next_num1 and num=next_num2;
