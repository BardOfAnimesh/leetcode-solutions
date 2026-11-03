-- ======================================
-- LeetCode Problem: game play analysis iv
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/game-play-analysis-iv/
-- Synced by: LinkCode
-- Date: 11/3/2026, 8:37:12 PM
-- ======================================


# Write your MySQL query statement below
with activitylog as(
    select player_id, 
    event_date,
    lead(event_date,1) over (partition by player_id order by player_id,event_date) as next_date,
    row_number() over(partition by player_id order by player_id,event_date) as rn
    
    from Activity
)

select round(count(distinct player_id)/ (select count( distinct player_id) from Activity),2) as fraction from activitylog where 
datediff(next_date, event_date)=1 and rn=1;