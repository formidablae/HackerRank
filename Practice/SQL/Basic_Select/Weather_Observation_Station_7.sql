/*
Enter your query here.
*/

SELECT DISTINCT CITY FROM STATION
WHERE (CITY LIKE '%a' OR
       CITY LIKE '%e' OR
       CITY LIKE '%o' OR
       CITY LIKE '%i' OR
       CITY LIKE '%u'
      )
