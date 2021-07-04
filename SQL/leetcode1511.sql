/* Write your PL/SQL query statement below */
SELECT june.customer_id, june.name
FROM   (SELECT c.customer_id, c.name, SUM(p.price * o.quantity) AS spent_money
        FROM   Customers c, Product p, Orders o
        WHERE  c.customer_id = o.customer_id
        AND    p.product_id = o.product_id
        AND    TO_CHAR(order_date, 'YYYY-MM') = ('2020-06')
        GROUP BY c.customer_id, c.name
        HAVING SUM(p.price * o.quantity) >= 100) june, 
       (SELECT c.customer_id, c.name, SUM(p.price * o.quantity) AS spent_money
        FROM   Customers c, Product p, Orders o
        WHERE  c.customer_id = o.customer_id
        AND    p.product_id = o.product_id
        AND    TO_CHAR(order_date, 'YYYY-MM') = ('2020-07')
        GROUP BY c.customer_id, c.name
        HAVING SUM(p.price * o.quantity) >= 100) july
WHERE  june.customer_id = july.customer_id
ORDER BY june.customer_id;
