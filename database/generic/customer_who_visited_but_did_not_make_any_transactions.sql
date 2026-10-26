-- ======================================
-- LeetCode Problem: customer who visited but did not make any transactions
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
-- Synced by: LinkCode
-- Date: 10/26/2026, 6:55:06 PM
-- ======================================


# Write your MySQL query statement below
select v.customer_id,count(v.customer_id) as count_no_trans  from Visits as v where not exists  (select 1 from Transactions as t where v.visit_id=t.visit_id )
group by v.customer_id;