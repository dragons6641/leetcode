/* Write your PL/SQL query statement below */
SELECT extra AS report_reason, COUNT(DISTINCT post_id) AS report_count
FROM   Actions
WHERE  action = 'report'
AND    TO_CHAR(action_date, 'YYYYMMDD') = '20190704'
GROUP BY action_date, extra;
