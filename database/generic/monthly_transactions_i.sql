-- ======================================
-- LeetCode Problem: monthly transactions i
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/monthly-transactions-i/
-- Synced by: LinkCode
-- Date: 10/28/2026, 9:54:38 PM
-- ======================================


# Write your MySQL query statement below

select
Date_format(trans_date,'%Y-%m') as month,
country,
count(*) as trans_count,
sum(case
    when
        state='approved' then 1 
        else 0 END ) as approved_count,
sum(amount) as trans_total_amount,
sum(case when state='approved' then amount else 0 end)as approved_total_amount
from Transactions group by Date_format(trans_date,"%Y-%m"),country;