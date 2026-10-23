-- ======================================
-- LeetCode Problem: customers who never order
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/customers-who-never-order/
-- Synced by: LinkCode
-- Date: 10/23/2026, 7:11:22 PM
-- ======================================


# Write your MySQL query statement below

select name as Customers from customers as c
where NOT EXISTS(
    select * from orders as o
    where o.customerId=c.id
)