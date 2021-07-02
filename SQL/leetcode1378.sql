/* Write your PL/SQL query statement below */
SELECT euni.unique_id, e.name
FROM   Employees e, EmployeeUNI euni
WHERE  e.id = euni.id(+);
