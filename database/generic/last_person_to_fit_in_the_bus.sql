-- ======================================
-- LeetCode Problem: last person to fit in the bus
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/last-person-to-fit-in-the-bus/
-- Synced by: LinkCode
-- Date: 11/21/2026, 11:13:44 PM
-- ======================================


# Write your MySQL query statement below
with lastguy as (
    select person_id,person_name,
    weight,turn,
    sum(weight) over (order by turn) as total_weight
    from Queue
)
select person_name from lastguy where total_weight<=1000 order by total_weight desc
limit 1