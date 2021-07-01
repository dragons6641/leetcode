/* Write your PL/SQL query statement below */
SELECT p.product_id, ROUND(SUM(p.price * us.units) / SUM(us.units), 2) AS average_price
FROM   Prices p, UnitsSold us
WHERE  p.product_id = us.product_id
AND    p.start_date <= us.purchase_date
AND    p.end_date >= us.purchase_date
GROUP BY p.product_id
ORDER BY p.product_id;
