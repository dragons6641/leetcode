/* Write your PL/SQL query statement below */
WITH   Ordered_Activity AS
(SELECT player_id, event_date, ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS rn
 FROM   Activity)
SELECT player_id, to_char(event_date, 'yyyy-mm-dd') AS first_login
FROM   Ordered_Activity
WHERE  rn = 1;
