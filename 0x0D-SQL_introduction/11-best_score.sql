-- List Records with Score >= 10
-- This script lists all records in the "second_table" with a score greater than or equal to 10 in the "hbtn_0c_0" database.

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
