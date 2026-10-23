-- ======================================
-- LeetCode Problem: duplicate emails
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/duplicate-emails/
-- Synced by: LinkCode
-- Date: 10/23/2026, 7:53:10 PM
-- ======================================


# Write your MySQL query statement below
select distinct email as Email from Person as e
where(
    select count(*) from Person as r where
    e.email=r.email
)>1;