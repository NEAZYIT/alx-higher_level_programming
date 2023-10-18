# SQL More Queries

This repository contains SQL scripts for various tasks involving MySQL databases. These tasks are related to managing privileges, creating tables, and querying data.

## Requirements

- Operating System: Ubuntu 20.04 LTS
- MySQL Version: 8.0 (version 8.0.25)
- Allowed Editors: vi, vim, emacs
- All SQL queries should be in uppercase (SELECT, WHERE...)
- All SQL files should have comments describing the tasks
- Files should end with a new line
- Create a README.md file at the root of the project

## Installation

To install MySQL 8.0 on Ubuntu 20.04 LTS, use the following commands:

```bash
sudo apt update
sudo apt install mysql-server
```
To connect to your MySQL server:
```bash
sudo mysql
```
Use "container-on-demand" to run MySQL with credentials root/root in the container. To start MySQL, run:
```bash
service mysql start
```
## Tasks

### Task 0: My privileges!

**Description:** List privileges of MySQL users user_0d_1 and user_0d_2.

### Task 1: Root user

**Description:** Create the MySQL server user user_0d_1 with all privileges and set the password.

### Task 2: Read user

**Description:** Create the database hbtn_0d_2 and the user user_0d_2 with SELECT privilege.

### Task 3: Always a name

**Description:** Create the table force_name in MySQL with specific columns.

### Task 4: ID can't be null

**Description:** Create the table id_not_null in MySQL with specific columns.

### Task 5: Unique ID

**Description:** Create the table unique_id in MySQL with specific columns.

### Task 6: States table

**Description:** Create the database hbtn_0d_usa and the table states in MySQL.

### Task 7: Cities table

**Description:** Create the database hbtn_0d_usa and the table cities in MySQL.

### Task 8: Cities of California

**Description:** List all cities of California from the database.

### Task 9: Cities by States

**Description:** List all cities contained in the database hbtn_0d_usa.

### Task 10: Genre ID by show

**Description:** List shows with at least one genre linked.

### Task 11: Genre ID for all shows

**Description:** List all shows along with their genre, displaying NULL for shows without a genre.

### Task 12: No genre

**Description:** List shows without a genre linked.

### Task 13: Number of shows by genre

**Description:** List all genres and the number of shows linked to each.

### Task 14: My genres

**Description:** List all genres of the show Dexter.

### Task 15: Only Comedy

**Description:** List all Comedy shows from the database.

### Task 16: List shows and genres

**Description:** List all shows and their linked genres from the database.


**Author**:

[NEAZYIT](https://github.com/NEAZYIT)
