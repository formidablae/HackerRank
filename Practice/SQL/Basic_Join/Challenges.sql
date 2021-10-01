/*
Enter your query here.
*/
SELECT H.hacker_id AS HackerID,
       H.name AS HackerName,
       count(C.challenge_id) AS ChallengesCreated
FROM Hackers H
JOIN Challenges C ON H.hacker_id = C.hacker_id
GROUP BY H.hacker_id, H.name
HAVING 
    ChallengesCreated = (SELECT MAX(temp1.cnt) from (
        SELECT COUNT(hacker_id) as cnt
        from Challenges
        group by hacker_id
        order by hacker_id) temp1)

    OR ChallengesCreated IN 
        (select t.cnt
         from (select count(*) as cnt 
               from challenges
               group by hacker_id) t
         group by t.cnt
         having count(t.cnt) = 1)
ORDER BY ChallengesCreated DESC, HackerID ASC;

