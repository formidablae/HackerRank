/*
Enter your query here.
*/
SELECT cast(round(min(LAT_N), 4) as decimal(10,4)) FROM STATION
WHERE LAT_N > 38.7780

