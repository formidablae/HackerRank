/*
Enter your query here.
*/

SELECT DISTINCT CITY FROM STATION
WHERE (CITY NOT LIKE 'a%' AND
       CITY NOT LIKE 'e%' AND
       CITY NOT LIKE 'u%' AND
       CITY NOT LIKE 'i%' AND
       CITY NOT LIKE 'o%') OR
      (CITY NOT LIKE '%a' AND
       CITY NOT LIKE '%e' AND
       CITY NOT LIKE '%u' AND
       CITY NOT LIKE '%i' AND
       CITY NOT LIKE '%o')
