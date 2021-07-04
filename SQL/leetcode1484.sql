/* Write your PL/SQL query statement below */
SELECT TO_CHAR(distinct_sell_date, 'YYYY-MM-DD') AS sell_date, COUNT(product) AS num_sold, 
       LISTAGG(product, ',') WITHIN GROUP (ORDER BY product) AS products
FROM   (SELECT DISTINCT sell_date AS distinct_sell_date, product
        FROM   Activities)
GROUP BY distinct_sell_date
ORDER BY distinct_sell_date;
