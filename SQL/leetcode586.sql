/* Write your PL/SQL query statement below */
SELECT customer_number
FROM   (SELECT COUNT(order_number) AS order_cnt, customer_number
        FROM   Orders
        GROUP BY customer_number
        ORDER BY order_cnt DESC)
WHERE  ROWNUM = 1;
