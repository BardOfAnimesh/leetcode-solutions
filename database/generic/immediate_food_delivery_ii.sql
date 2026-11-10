-- ======================================
-- LeetCode Problem: immediate food delivery ii
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/immediate-food-delivery-ii/
-- Synced by: LinkCode
-- Date: 11/10/2026, 9:42:32 PM
-- ======================================


# Write your MySQL query statement below
SELECT 
    ROUND(AVG(order_date = customer_pref_delivery_date) * 100, 2) as immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date) as first_order
    FROM Delivery
    GROUP BY customer_id
);