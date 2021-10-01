/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT CITY.Name FROM City
JOIN Country ON CITY.CountryCode = COUNTRY.Code
WHERE Country.Continent = 'Africa'
