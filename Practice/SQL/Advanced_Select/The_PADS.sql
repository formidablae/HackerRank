/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT Name + "(" + SUBSTRING(Occupation,1,1) + ")" FROM OCCUPATIONS
ORDER BY Name;
SELECT "There are a total of " + cast(COUNT(Occupation) as varchar) + " " + LOWER(Occupation) + "s." FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(Occupation) ASC, Occupation ASC;

