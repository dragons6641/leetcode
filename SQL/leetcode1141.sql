/* Write your PL/SQL query statement below */
SELECT TO_CHAR(activity_date, 'YYYY-MM-DD') AS day, COUNT(DISTINCT user_id) AS active_users
FROM   Activity
WHERE  (TO_DATE('2019-07-27', 'YYYY-MM-DD') - activity_date) < 30
GROUP BY activity_date
ORDER BY activity_date;
