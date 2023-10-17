-- List Records with Score and Name (with Name Filter)
-- This script lists all records with a name value in the "second_table" of the "hbtn_0c_0" database.

-- List records with score and name, filtering out rows without a name value, and ordering by descending score.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
