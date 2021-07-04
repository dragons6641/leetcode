/* Write your PL/SQL query statement below */
SELECT DISTINCT c.title
FROM   TVProgram tv, Content c
WHERE  tv.content_id = c.content_id
AND    TO_CHAR(tv.program_date, 'YYYY-MM') = '2020-06'
AND    c.Kids_content = 'Y'
AND    c.content_type = 'Movies'
ORDER BY c.title;
