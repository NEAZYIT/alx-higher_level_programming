# SQL Introduction - Project README

## Description
This project involves a series of SQL tasks for managing databases using MySQL 8.0 on Ubuntu 20.04 LTS. Each task is a separate SQL script with specific instructions and requirements.

## General Requirements
- All files must end with a new line.
- All SQL queries should have a comment just before.
- All files should start with a comment describing the task.
- All SQL keywords should be in uppercase (e.g., SELECT, WHERE).
- A README.md file at the root of the project is mandatory.
- File length will be tested using wc.

## Database Configuration
- MySQL 8.0 is used on Ubuntu 20.04 LTS.
- Credentials: root/root
- You can use "container-on-demand" to run MySQL.

## Tasks

### 0. List Databases
- Task: Write a script to list all databases.
- File: [0-list_databases.sql](/0x0D-SQL_introduction/0-list_databases.sql)

### 1. Create a Database
- Task: Write a script to create the database "hbtn_0c_0" if it doesn't exist.
- File: [1-create_database_if_missing.sql](/0x0D-SQL_introduction/1-create_database_if_missing.sql)

### 2. Delete a Database
- Task: Write a script to delete the database "hbtn_0c_0" if it exists.
- File: [2-remove_database.sql](/0x0D-SQL_introduction/2-remove_database.sql)

### 3. List Tables
- Task: Write a script to list all tables of a specified database.
- File: [3-list_tables.sql](/0x0D-SQL_introduction/3-list_tables.sql)

### 4. First Table
- Task: Create a table called "first_table" with specific columns.
- File: [4-first_table.sql](/0x0D-SQL_introduction/4-first_table.sql)

### 5. Full Table Description
- Task: Print the full description of the "first_table" in the specified database.
- File: [5-full_table.sql](/0x0D-SQL_introduction/5-full_table.sql)

### 6. List All in Table
- Task: List all rows of the "first_table" in the specified database.
- File: [6-list_values.sql](/0x0D-SQL_introduction/6-list_values.sql)

### 7. First Add
- Task: Insert a new row in the "first_table."
- File: [7-insert_value.sql](/0x0D-SQL_introduction/7-insert_value.sql)

### 8. Count 89
- Task: Display the number of records with id = 89 in the "first_table."
- File: [8-count_89.sql](/0x0D-SQL_introduction/8-count_89.sql)

### 9. Full Creation
- Task: Create a table "second_table" and add multiple rows.
- File: [9-full_creation.sql](/0x0D-SQL_introduction/9-full_creation.sql)

### 10. List by Best
- Task: List all records of "second_table" ordered by score.
- File: [10-top_score.sql](/0x0D-SQL_introduction/10-top_score.sql)

### 11. Select the Best
- Task: List records with a score >= 10 in "second_table."
- File: [11-best_score.sql](/0x0D-SQL_introduction/11-best_score.sql)

### 12. Cheating is Bad
- Task: Update the score of a record named "Bob" to 10 in "second_table."
- File: [12-no_cheating.sql](/0x0D-SQL_introduction/12-no_cheating.sql)

### 13. Score Too Low
- Task: Remove records with a score <= 5 in "second_table."
- File: [13-change_class.sql](/0x0D-SQL_introduction/13-change_class.sql)

### 14. Average
- Task: Compute the score average of all records in "second_table."
- File: [14-average.sql](/0x0D-SQL_introduction/14-average.sql)

### 15. Number by Score
- Task: List the number of records with the same score in "second_table."
- File: [15-groups.sql](/0x0D-SQL_introduction/15-groups.sql)

### 16. Say My Name
- Task: List records of "second_table" with names, ordered by score.
- File: [16-no_link.sql](/0x0D-SQL_introduction/16-no_link.sql)

## Authors
- [NEAZYIT](https://github.com/NEAZYIT)
