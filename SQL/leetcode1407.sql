/* Write your PL/SQL query statement below */
SELECT u.name, NVL(SUM(r.distance), 0) AS travelled_distance
FROM   Users u, Rides r
WHERE  u.id = r.user_id(+)
GROUP BY u.name
ORDER BY travelled_distance DESC, u.name ASC;
