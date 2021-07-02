/* Write your PL/SQL query statement below */
SELECT s.id, s.name
FROM   Students s
WHERE  s.id NOT IN (SELECT DISTINCT s.id
                    FROM   Departments d, Students s
                    WHERE  d.id = s.department_id);
