/* Write your PL/SQL query statement below */
SELECT MIN(ABS(x - prev_x)) AS shortest
FROM   (SELECT x, LAG(x) OVER (ORDER BY x) AS prev_x
        FROM   point
        ORDER BY x);
