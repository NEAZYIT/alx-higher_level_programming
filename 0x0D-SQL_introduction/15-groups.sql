-- Count Records by Score
-- This script counts the number of records with the same score in the "second_table" of the "hbtn_0c_0" database.

-- Count records by score and display the score and the number of records.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC, score DESC;
