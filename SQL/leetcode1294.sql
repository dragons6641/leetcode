/* Write your PL/SQL query statement below */
SELECT c.country_name, 
       CASE 
       WHEN AVG(w.weather_state) <= 15 THEN 'Cold'
       WHEN AVG(w.weather_state) >= 25 THEN 'Hot'
       ELSE 'Warm' END AS weather_type
FROM   Countries c, Weather w
WHERE  c.country_id = w.country_id
AND    TO_CHAR(w.day, 'YYYY-MM') = '2019-11'
GROUP BY c.country_name;
