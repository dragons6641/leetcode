/* Write your PL/SQL query statement below */
SELECT *
FROM   Users
WHERE  REGEXP_LIKE (mail, '^[A-Za-z][A-Za-z-0-9_.-]*@leetcode.com')
ORDER BY user_id;
