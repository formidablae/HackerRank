/*
Enter your query here.
*/

SELECT Name FROM STUDENTS
WHERE Marks > 75
ORDER BY SUBSTR(Name,-3), ID;

