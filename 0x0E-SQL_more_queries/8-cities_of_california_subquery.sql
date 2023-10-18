-- TASK: List all cities of California from the 'hbtn_0d_usa' database
-- List cities of CA

-- List all cities of California sorted by cities.id
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
