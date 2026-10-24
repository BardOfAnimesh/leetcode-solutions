-- ======================================
-- LeetCode Problem: classes with at least 5 students
-- Language: SQL (generic)
-- Link: https://leetcode.com/problems/classes-with-at-least-5-students/
-- Synced by: LinkCode
-- Date: 10/24/2026, 8:24:16 AM
-- ======================================


# Write your MySQL query statement below
Select distinct class from Courses group by class having count(class)>4;