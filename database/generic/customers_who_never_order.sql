-- ======================================
-- LeetCode Problem: customers who never order
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/customers-who-never-order/
-- Synced by: LinkCode
-- Date: 10/23/2026, 7:03:50 PM
-- ======================================


# Write your MySQL query statement below

select name as Customers from customers as c left join orders as o on c.id=o.customerId where o.customerId is NULL;
