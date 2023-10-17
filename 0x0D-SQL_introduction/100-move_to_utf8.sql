-- Convert character set and collate to UTF8 (utf8mb4_unicode_ci)
-- Convert the database: `hbtn_0c_0` to UTF8
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Change database
USE hbtn_0c_0;

-- Convert all and future columns in `first_table` to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
