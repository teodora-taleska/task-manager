# Project Title: Task Manager

Link to youtube: https://youtu.be/IgUcO-DDYWM


## Description

The Task Manager is a Python-based application that leverages Object-Oriented Programming to create an efficient task management system.

## Key Features

### Task Management

- Create, edit, delete, and mark tasks as complete or incomplete.
- Organize tasks into categories or projects (e.g., work, personal, shopping).

### User Authentication

- Implemented user sign-up, login, and logout functionality.

### Security

- Implemented secure password storage and authentication.
- Protect against common security vulnerabilities like SQL injection and XSS.

### Priority Levels

- Allow users to set priority levels (e.g., 1, 2, 3) for tasks.
- Implemented sorting and filtering based on priority.

### Search and Filter

- Implemented search and filter options to help users find tasks quickly.
- Filter tasks by name, category, priority, due date, and completion status.

### Data Persistence

- Used MySQL database hosted locally on XAMPP with phpMyAdmin.
- Implemented data models using SQLAlchemy for efficient data storage and retrieval.

### User Interface

- Created a user-friendly command-line interface for task management.

### Export and Import

- Users are allowed to export tasks to a file (e.g., CSV).

### Getting Started

#### Prerequisites

- Python 3.7 or higher
- XAMPP with MySQL and phpMyAdmin
- SQLAlchemy
- Other dependencies (specified in `requirements.txt`)

#### Installation

1. Clone the repository: `git clone https://gitlab.com/taleskateodora/task-manager.git`
2. Navigate to the project directory: `cd task-manager`
3. Activate the virtual environment:
```
    source venv/bin/activate
```
OR
```
    .\venv\Scripts\Activate.ps1
```
4. Install dependencies: `pip install -r requirements.txt`
5. Run the application: `python app.py`

### Usage

To start using Task Manager, follow these steps:

1. Register for an account or log in.
2. Create tasks with details like name, category, deadline, and priority.
3. Organize and filter tasks based on your needs.
4. Export your tasks to a CSV file for backup.
5. View tasks.
6. Delete tasks.
7. Log out.

### Contributing

I welcome contributions! If you find a bug, have a feature request, or want to contribute code, please [open an issue](https://github.com/taleskateodora/task-manager/issues) or [create a pull request](https://github.com/taleskateodora/task-manager/pulls).

### Acknowledgments

- SQLAlchemy for the database integration.
- XAMPP for hosting the local MySQL database.
