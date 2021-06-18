/* Write your PL/SQL query statement below */
SELECT DISTINCT a_seat_id AS seat_id
FROM   (SELECT a.seat_id AS a_seat_id, b.seat_id AS b_seat_id
        FROM   cinema a, cinema b
        WHERE  ABS(a.seat_id - b.seat_id) = 1
        AND    a.free = '1'
        AND    b.free = '1')
ORDER BY seat_id;
