-- Select the database first
USE hbtn_0c_0;

-- Convert hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- This script converts the specified database, table, and field to UTF8.

-- Set the database character set and collation to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Set the character set and collation for the first_table and its name field.
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Verify the changes.
SHOW CREATE TABLE first_table;
