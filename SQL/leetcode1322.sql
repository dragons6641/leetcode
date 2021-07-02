/* Write your PL/SQL query statement below */
SELECT ad_id, 
       ROUND(NVL(SUM(CASE WHEN action = 'Clicked' THEN 1 ELSE 0 END) / 
       DECODE(SUM(CASE WHEN action = 'Ignored' THEN 0 ELSE 1 END), 0, NULL, 
       SUM(CASE WHEN action = 'Ignored' THEN 0 ELSE 1 END)), 0) * 100, 2) AS ctr
FROM   Ads
GROUP BY ad_id
ORDER BY ctr DESC, ad_id ASC;
