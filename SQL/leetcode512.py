/* Write your PL/SQL query statement below */
WITH   Ordered_Activity AS
(SELECT player_id, device_id, ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS rn
 FROM   Activity)
SELECT player_id, device_id
FROM   Ordered_Activity
WHERE  rn = 1;
