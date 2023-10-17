-- Remove Records with Score <= 5
-- This script removes all records with a score less than or equal to 5 from the "second_table" of the "hbtn_0c_0" database.

-- Delete records with a score less than or equal to 5.
DELETE FROM second_table
WHERE score <= 5;
