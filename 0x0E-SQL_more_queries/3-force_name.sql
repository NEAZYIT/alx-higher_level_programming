-- Task: Create 'force_name' table with specified structure

-- Create the 'force_name' table if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
