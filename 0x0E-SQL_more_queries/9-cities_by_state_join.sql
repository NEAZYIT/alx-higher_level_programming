-- TASK: List all cities in the 'hbtn_0d_usa' database with their corresponding state names.
-- List all cities in the 'hbtn_0d_usa' database with their corresponding state names.


-- List all cities with their corresponding state names, sorted by cities.id
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
