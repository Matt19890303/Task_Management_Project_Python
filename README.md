# Task_Manager_Project

Task_manager_project is program that managers tasks by adding and reading information/credentials from and to a text file, 
allowing manipulation of the tasks at hand ad creating new tasks.

## Task

Build a management system that will allow the user to login as a user or admin to add, delete, edit and mark tasks as complete.
All manipulating text file data

## Run Locally

 - Run this command 'git clone https://github.com/Matt19890303/Task_Management_Project_Python.git'
 - I used Pycharm for this ad imported datetime modules ('import datetime', 'from datetime import date')
  - Make sure you have the text files that come with it


## Usage Example

```python
import datetime
from datetime import date

# Checks text file for credentials for login
Login below
Enter your username: admin
Enter your password: admin
Username and/or Password incorrect!
Enter your username: admin
Enter your password: adm1n
Username and Password correct! You have successfully logged in.

# From menu, allows user to see all tasks assigned to that specific user
Please select one of the following options:

        r  - register user
        ds - display statistics
        gr - generate reports
        a  - add task
        va - view all tasks
        vm - view my tasks
        e  - exit

        : vm
vm
Your reports have been generated successfully.
------------------------------------------

        Task 1:      
        Register Users with taskManager.py
        Assigned to:        admin
        Date assigned:      10 Oct 2019
        Due Date:           20 Oct 2019
        Task Complete?      Yes
        Task Description:


```

## Contributing
HyperionDev assisted me here with structure and logic.
