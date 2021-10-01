/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT cast(round(cast(sum(LAT_N) as DECIMAL(10,2)),2) as varchar) + " " + cast(round(cast(sum(LONG_W) as DECIMAL(10,2)),2) as varchar)
FROM STATION
