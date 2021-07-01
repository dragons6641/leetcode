/* Write your PL/SQL query statement below */
SELECT e.employee_id, ct.team_size
FROM   Employee e, 
       (SELECT team_id, COUNT(*) AS team_size
        FROM   Employee
        GROUP BY team_id) ct
WHERE  e.team_id = ct.team_id;
