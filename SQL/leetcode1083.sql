/* Write your PL/SQL query statement below */
SELECT DISTINCT buyer_id
FROM   Sales
WHERE  buyer_id in (SELECT DISTINCT s.buyer_id
                    FROM   Product p, Sales s
                    WHERE  p.product_id = s.product_id
                    AND    p.product_name = 'S8')
AND    buyer_id not in (SELECT DISTINCT s.buyer_id
                        FROM   Product p, Sales s
                        WHERE  p.product_id = s.product_id
                        AND    p.product_name = 'iPhone');
