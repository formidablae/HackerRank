/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT cast(round(SUM(LAT_N), 4, 1) as decimal(10,4)) FROM STATION
WHERE LAT_N > 38.7880 AND LAT_N < 137.2345

