/* Write your PL/SQL query statement below */
SELECT ROUND(
       (SELECT COUNT(*) AS immediate_count
        FROM   Delivery
        WHERE  order_date = customer_pref_delivery_date) * 100 / 
       (SELECT COUNT(*) AS total_count
        FROM   Delivery), 2) AS immediate_percentage
FROM   Delivery
WHERE  ROWNUM = 1;
