/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT COUNTRY.CONTINENT, ROUND(SUM(CITY.POPULATION)/COUNT(CITY.ID),1) FROM CITY
JOIN COUNTRY ON COUNTRY.CODE = CITY.COUNTRYCODE
GROUP BY COUNTRY.CONTINENT

