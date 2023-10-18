-- Task: Create 'id_not_null' table with specified structure

-- Create the 'id_not_null' table if it doesn't exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
