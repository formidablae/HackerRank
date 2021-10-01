/*
Enter your query here.
*/

SELECT Name, Grade, Marks FROM Students, Grades
WHERE Marks >= 70 AND Marks >= Min_Mark AND Marks <= Max_Mark
ORDER BY Grade DESC, Name ASC;

SELECT Name=NULL, Grade, Marks FROM Students, Grades
WHERE Marks < 70 AND Marks >= Min_Mark AND Marks <= Max_Mark
ORDER BY Grade DESC, Marks ASC;

