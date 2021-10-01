/*
Enter your query here.
*/
SELECT N, CASE
            WHEN P is NULL THEN "Root"
            WHEN N IN (SELECT P FROM BST) THEN "Inner"
            ELSE "Leaf"
          END AS NodeType
FROM BST
ORDER BY N ASC

