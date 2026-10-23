-- ======================================
-- LeetCode Problem: duplicate emails
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/duplicate-emails/
-- Synced by: LinkCode
-- Date: 10/23/2026, 8:00:21 PM
-- ======================================


# Write your MySQL query statement below
select distinct email as Email from Person group by email having count(*)>1