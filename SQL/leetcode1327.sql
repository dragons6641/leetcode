/* Write your PL/SQL query statement below */
SELECT r.product_name, r.unit
FROM   (SELECT p.product_id, p.product_name, SUM(o.unit) AS unit
        FROM   Products p, Orders o
        WHERE  p.product_id = o.product_id
        AND    TO_CHAR(o.order_date, 'YYYY-MM') = '2020-02'
        GROUP BY p.product_id, p.product_name
        ORDER BY p.product_id) r
WHERE  r.unit >= 100;
