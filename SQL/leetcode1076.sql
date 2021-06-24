/* Write your PL/SQL query statement below */
SELECT project_id
FROM   (SELECT project_id, COUNT(*) AS employee_count
        FROM   Project
        GROUP BY project_id)
WHERE  employee_count = (SELECT MAX(COUNT(*))
                         FROM   Project
                         GROUP BY project_id);
