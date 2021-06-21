/* Write your PL/SQL query statement below */
SELECT s.name
FROM   salesperson s
WHERE  s.sales_id NOT IN (SELECT o.sales_id
                          FROM   company c, orders o
                          WHERE  c.com_id = o.com_id
                          AND    c.name = 'RED');
