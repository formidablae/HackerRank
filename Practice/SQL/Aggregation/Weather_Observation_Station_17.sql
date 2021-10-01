/*
Enter your query here.
*/
SELECT cast(round(LONG_W, 4) as decimal(10,4)) FROM STATION
WHERE LAT_N > 38.7780
ORDER BY LAT_N ASC LIMIT 1;

