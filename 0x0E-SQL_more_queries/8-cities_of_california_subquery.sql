-- TASK: List all cities of California from the 'hbtn_0d_usa' database
-- List cities of CA

-- Use the 'hbtn_0d_usa' database
USE hbtn_0d_usa;

-- Find the id of California in the 'states' table
SET @california_id = (SELECT id FROM states WHERE name = 'California');

-- List all cities of California sorted by cities.id
SELECT * FROM cities
WHERE state_id = @california_id
ORDER BY id;
