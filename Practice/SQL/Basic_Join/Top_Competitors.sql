/*
Enter your query here.
*/
SELECT hackers.hacker_id, hackers.name FROM hackers
JOIN submissions
JOIN challenges
JOIN difficulty
ON (submissions.hacker_id = hackers.hacker_id
    AND submissions.challenge_id = challenges.challenge_id
    AND challenges.difficulty_level = difficulty.difficulty_level)
WHERE submissions.score = difficulty.score
GROUP BY hackers.hacker_id, hackers.name
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC, hackers.hacker_id ASC;

