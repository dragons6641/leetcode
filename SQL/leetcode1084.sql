/* Write your PL/SQL query statement below */
SELECT p.product_id, p.product_name
FROM   Product p
WHERE  p.product_id not in (SELECT DISTINCT s.product_id
                            FROM   Sales s
                            WHERE  '20190101' > TO_CHAR(s.sale_date, 'YYYYMMDD')
                            OR     '20190331' < TO_CHAR(s.sale_date, 'YYYYMMDD'));
