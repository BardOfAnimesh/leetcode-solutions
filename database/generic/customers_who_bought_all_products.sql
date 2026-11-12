-- ======================================
-- LeetCode Problem: customers who bought all products
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/customers-who-bought-all-products/
-- Synced by: LinkCode
-- Date: 11/13/2026, 2:05:49 AM
-- ======================================


# Write your MySQL query statement below
with custcount as (
    select customer_id, count( distinct product_key)as pro_count from Customer group by customer_id
)

select customer_id from custcount where pro_count=(select count(*)from product)