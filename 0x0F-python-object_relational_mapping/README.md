# Object-Relational Mapping with Python

## Overview
This project explores the implementation of Object-Relational Mapping (ORM) in Python using MySQL databases. Each script corresponds to specific tasks that involve database operations, SQL queries, and ORM concepts.

---

## Requirements
### General Information
- **Editors:** vi, vim, emacs
- **Interpreter/Compiler:** Ubuntu 20.04 LTS using python3 (version 3.8.5)
- **Execution:** MySQLdb version 2.0.x, SQLAlchemy version 1.4.x
- **File Endings:** All files should end with a new line
- **First Line in Files:** `#!/usr/bin/python3`

### Coding Standards and Modules
- **Code Formatting:** pycodestyle (version 2.8.*)
- **Execution Permission:** All files must be executable
- **Documentation:** Detailed documentation for modules, classes, and functions
- **MySQL Execution:** Avoid using execute with sqlalchemy

---

## Task Details

### Task 0: Get all states
#### File: `0-select_states.py`
- **Description:** Lists all states from the database hbtn_0e_0_usa
- **Arguments:** MySQL username, MySQL password, database name
- **Modules:** MySQLdb
- **Sorting:** Ascending order by states.id

### Task 1: Filter states
#### File: `1-filter_states.py`
- **Description:** Lists all states starting with 'N' from hbtn_0e_0_usa
- **Arguments:** MySQL username, MySQL password, database name
- **Modules:** MySQLdb
- **Sorting:** Ascending order by states.id

### Task 2: Filter states by user input
#### File: `2-my_filter_states.py`
- **Description:** Displays states based on user input matching the name in hbtn_0e_0_usa
- **Arguments:** MySQL username, MySQL password, database name, state name searched
- **Modules:** MySQLdb
- **Sorting:** Ascending order by states.id

### Task 3: SQL Injection...
#### File: `2-my_filter_states.py` (updated)
- **Description:** Secure version of the script to prevent SQL injection
- **Arguments:** MySQL username, MySQL password, database name, state name searched (safe from injection)
- **Modules:** MySQLdb
- **Sorting:** Ascending order by states.id

### Task 4: Cities by states
#### File: `4-cities_by_state.py`
- **Description:** Lists all cities from the database hbtn_0e_4_usa
- **Arguments:** MySQL username, MySQL password, database name
- **Modules:** MySQLdb
- **Sorting:** Ascending order by cities.id

### Task 5: All cities by state
#### File: `5-filter_cities.py`
- **Description:** Lists all cities of a given state from the database hbtn_0e_4_usa
- **Arguments:** MySQL username, MySQL password, database name, state name (SQL injection free)
- **Modules:** MySQLdb
- **Sorting:** Ascending order by cities.id

### Task 6: First state model
#### File: `model_state.py`
- **Description:** Class definition of a State using SQLAlchemy
- **Attributes:** id (auto-generated, unique integer), name (string, max 128 characters)
- **Modules:** SQLAlchemy

### Task 7: All states via SQLAlchemy
#### File: `7-model_state_fetch_all.py`
- **Description:** Lists all State objects from the database hbtn_0e_6_usa
- **Arguments:** MySQL username, MySQL password, database name
- **Modules:** SQLAlchemy
- **Sorting:** Ascending order by states.id

### Task 8: First state
#### File: `8-model_state_fetch_first.py`
- **Description:** Prints the first State object from the database hbtn_0e_6_usa
- **Arguments:** MySQL username, MySQL password, database name
- **Modules:** SQLAlchemy

### Task 9: Contains 'a'
#### File: `9-model_state_filter_a.py`
- **Description:** Lists all State objects containing the letter 'a' from the database hbtn_0e_6_usa
- **Arguments:** MySQL username, MySQL password, database name
- **Modules:** SQLAlchemy
- **Sorting:** Ascending order by states.id

### Task 10: Get a state
#### File: `10-model_state_my_get.py`
- **Description:** Prints the State object with the given name from the database hbtn_0e_6_usa
- **Arguments:** MySQL username, MySQL password, database name, state name to search (SQL injection free)
- **Modules:** SQLAlchemy

### Task 11: Add a new state
#### File: `11-model_state_insert.py`
- **Description:** Adds the State object "Louisiana" to the database hbtn_0e_6_usa
- **Arguments:** MySQL username, MySQL password, database name
- **Modules:** SQLAlchemy

### Task 12: Update a state
#### File: `12-model_state_update_id_2.py`
- **Description:** Changes the name of a State object with id = 2 to "New Mexico"
- **Arguments:** MySQL username, MySQL password, database name
- **Modules:** SQLAlchemy

### Task 13: Delete states
#### File: `13-model_state_delete_a.py`
- **Description:** Deletes all State objects containing the letter 'a' from the database hbtn_0e_6_usa
- **Arguments:** MySQL username, MySQL password, database name
- **Modules:** SQLAlchemy

### Task 14: Cities in state
#### Files: `model_city.py`, `14-model_city_fetch_by_state.py`
- **Description:** Defines City class and prints all City objects from hbtn_0e_14_usa grouped by state
- **Arguments:** MySQL username, MySQL password, database name

---

## Usage
- Clone the repository: `git clone <repository_link>`
- Navigate to the project directory: `cd alx-higher_level_programming/0x0F-python-object_relational_mapping`
- Run the desired script with appropriate arguments

---

## Installation
### venv Setup
- Install venv: `sudo apt-get install python3.8-venv`
- Create venv: `python3 -m venv venv`
- Activate venv: `source venv/bin/activate`

### MySQLdb and SQLAlchemy Setup
- MySQLdb Installation:
  - Install dependencies: `sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev`
  - Install MySQLdb: `sudo pip3 install mysqlclient`
- SQLAlchemy Installation: `sudo pip3 install SQLAlchemy`

---

## Notes
- Take care to avoid SQL injection vulnerabilities
- Ignore warning messages related to deprecated functionalities in SQLAlchemy

---

## Contribution
- Fork the repository
- Create a new branch (`git checkout -b feature`)
- Make appropriate changes and commit them (`git commit -am 'Add new feature'`)
- Push to the branch (`git push origin feature`)
- Create a pull request

---

## Credits

[NEAZYIT](https://github.com/NEAZYIT)
