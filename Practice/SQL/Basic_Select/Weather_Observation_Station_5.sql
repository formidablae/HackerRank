/*
Enter your query here.
*/

SELECT CITY, LENGTH(CITY) AS CITYNAME_LENGTH FROM STATION
ORDER BY CITYNAME_LENGTH ASC, CITY ASC LIMIT 1;

SELECT CITY, LENGTH(CITY) AS CITYNAME_LENGTH FROM STATION
ORDER BY CITYNAME_LENGTH DESC, CITY ASC LIMIT 1;
