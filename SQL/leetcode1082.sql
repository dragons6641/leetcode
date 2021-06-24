/* Write your PL/SQL query statement below */
SELECT seller_id
FROM   (SELECT seller_id, SUM(price) AS total_price
        FROM   Sales
        GROUP BY seller_id)
WHERE  total_price = (SELECT MAX(SUM(price))
                      FROM   Sales
                      GROUP BY seller_id);
