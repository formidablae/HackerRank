/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT sum(CITY.POPULATION) FROM CITY
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
where COUNTRY.CONTINENT = 'Asia';

