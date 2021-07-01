/* Write your PL/SQL query statement below */
SELECT jt.student_id, jt.student_name, jt.subject_name, COUNT(e.student_id) AS attended_exams
FROM   (SELECT Students.student_id, Students.student_name, Subjects.subject_name
        FROM   Students, Subjects, Examinations
        GROUP BY Students.student_id, Students.student_name, Subjects.subject_name) jt, 
        Examinations e
WHERE  jt.student_id = e.student_id(+)
AND    jt.subject_name = e.subject_name(+)
GROUP BY jt.student_id, jt.student_name, jt.subject_name
ORDER BY jt.student_id, jt.subject_name;
