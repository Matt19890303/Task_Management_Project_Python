# Importing datetime and dates to enable the comparison and to retrieve the current date.
import datetime
from datetime import date

# If username is admin print the following menu option
# Option 'r' is selected then registration process
# Only username and password of 'admin' and 'adm1n'
def reg_user():
    authorised = False
    f = open('user.txt', 'r')
    if user_choice == 'r':
        new_username = input("Enter new username: ")
        new_username = new_username.strip()
        while True:
            for i in f:
                login_info = i.strip().split(', ')
                if new_username == login_info[0]:
                    authorised = True
            if authorised == True:
                print("Username already exists! Try a different Username.")
                new_username = input("Enter new username: ")
                authorised = False
            else:
                new_password = input("Enter password: ")
                confirm_password = input("Please confirm your password: ")
                # Adds the new username and password registered to the user text file
                if confirm_password == new_password:
                    print("\nNew User Added!")
                    u = open('user.txt', 'a')
                    u.write(f'\n{new_username}, {new_password}')
                    u.close()
                    print(user_choice)
                    break
                else:
                    print("Password does not match!")



# Check the the user choice for 'ds'
# Checks tasks text file and prints all the usernames and tasks from tasks text file
def display_stats():
    if user_choice == 'ds':
        print(generate_reports())  # Calling function generate files in case they do no exist yet.
        print("""\n____________________________________________________
        The task overview report is as follows:
        ____________________________________________________\n""")  # Heading printed for user-friendly display.
        with open('task_overview.txt', 'r+') as f3:  # Opening the task_overview file to get info from it.
            for line in f3:
                print(line)  # Printing/displaying each line in the file.
        print("""\n_____________________________________________________
        The user overview report is as follows:
        _____________________________________________________\n""")  # Heading printed for user_friendly display.
        with open('user_overview.txt', 'r+') as f4:  # Opening user_overview file.
            for line in f4:
                print(line)  # Displaying each line of the file.
        print("""\n______________________________________________________

        End of Statistics Reports
        ______________________________________________________\n""")  # End of reports display.



# Option 'a' is selected then registration process
# Asks user to add in different details about the tasks info
def add_task():
    if user_choice == 'a':
        assigned_to = input("Enter the username of the person the task is assigned to: ")
        task_title = input("Enter the title of the task: ")
        task_description = input("Enter the description of the task: ")
        due_date = input("Enter due date for the task (e.g. 12 May 2020): ")
        assigned_date = input("Enter assigned date for the task (e.g. 12 May 2020): ")
        task_completed = "No"
        task_list = f'{assigned_to}, {task_title}, {task_description}, {assigned_date}, {due_date}, {task_completed}'
        f = open('tasks.txt', 'a')
        f.write(task_list)
        f.close()
        print("\nNew Task Added!")


# Prints out all the tasks from task text file
def view_all():
    if user_choice == "va":
        task_count = 0
        for key in tasks_dict:
            task_count += 1
            print(f"""____________________________________________

Task {str(task_count)}:     {str(tasks_dict[key][1])}
Assigned to:            {str(tasks_dict[key][0])}
Date assigned:          {str(tasks_dict[key][3])}
Due Date:               {str(tasks_dict[key][4])}
Task Complete?          {str(tasks_dict[key][5])}
Task Description:
 {str(tasks_dict[key][2])}
________________________________________________""")

    return "End of Tasks."

# This function compares the due date in the task file and current date,
# Checks if the current date is greater than the due date, then the task is over due.
def over_due_check(due_date):
    # Boolean varible for a comparison check
    over_due = False

    # The dates in this task are in the format '10 Dec 2015' as a string,So, this needs to be converted to integers to compare dates.
    # First, the variable is split into a list.
    list_dates = due_date.split()

    # The first item is cast into an integer and stored in the 'day' variable.
    day = int(list_dates[0])
    # The second item is cast into an integer and stored in the 'year' variable.
    year = int(list_dates[2])

    # A month dictionary with number values is set to enable calculation of string month into an integer.
    months_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
                   'Nov': 11, 'Dec': 12}

    # The value of the key in months_dict which is stored in the variable 'month'.
    # This will be a number value from the appropriate key in months_dict.
    month = months_dict[list_dates[1][0:3]]

    # Used this link to assist me with structure - https://www.programiz.com/python-programming/datetime
    # Getting the current date using the datetime module and formatting it into the same format at the due date initially was.
    date_now = datetime.date.today().strftime('%d %b %Y')

    # The date here is split into a list of items.
    date_now_list = date_now.split()

    # The first item is stored as an integer in day_2.
    day_2 = int(date_now_list[0])
    # Second item is stored as an integer in year_2.
    year_2 = int(date_now_list[2])
    # The corresponding integer value from months_dict at appropriate key is stored in 'month_2'.
    month_2 = months_dict[date_now_list[1]]

    # Now that we have integers for year, day and month to work with, two dates can be created in the correct format for comparison.
    # date_1 is the due date and date_2 is the current date.
    date_1 = date(year, month, day)
    date_2 = date(year_2, month_2, day_2)

    # If current date is greater than set due date, over_due is changed to 'True'.
    if date_2 > date_1:
        over_due = True
        return over_due

    # If set due date is greater than current date, over_due is 'False'.
    elif date_1 > date_2 or date_1 == date_2:
        over_due = False
        return over_due


def generate_reports():
    # Setting blank strings to store info in to be written to the generated text files.
    task_overview = ""
    user_overview = ""
    # tasks_total = len(tasks_dict)  # Total number of tasks is equal to the key count of tasks_dict.
    # Adding a string with the total tasks number to the tas_overview string.
    task_overview = task_overview + f"The total number of tasks generated and tracked by task_manager.py is {str(len(tasks_dict))}."
    # Setting variables for integers concerning complete tasks, incomplete tasks and overdue tasks respectively.
    x = 0
    y = 0
    z = 0

    for key in tasks_dict:
        # Checking for which tasks are complete by finding the 'Yes' string in each key of tasks_dict.
        if tasks_dict[key][5] == "Yes":
            # If the task is complete, i.e. 'Yes' string item is present, variable x is increased by 1.
            x += 1
            # Checking for which tasks are complete by finding the 'No' string in each key of tasks_dict.
        elif tasks_dict[key][5] == "No":
            # If the task is complete, i.e. 'No' string item is present, variable y is increased by 1.
            y += 1
            # If the over_due_check function returns 'True', a task is overdue and incomplete.
            if over_due_check(tasks_dict[key][4]):
                z += 1  # 'z' is increased by 1 to count the incomplete, overdue tasks.
    # All of the numbers calculated above are now built into sentences in the task_overview string.
    # Percentages are also calculated within the f-strings added, with the results being rounded to 2 decimal places and cast into strings into sentences.
    task_overview = task_overview + f"\nThe total number of completed tasks is {str(x)}." + f"\nThe total number of incomplete tasks is {str(y)}."
    task_overview = task_overview + f"\nThe total number of incomplete and overdue tasks is {str(z)}."
    task_overview = task_overview + f"\nThe percentage of incomplete tasks is {str(round((y / len(tasks_dict)) * 100, 2))}%."
    task_overview = task_overview + f"\nThe percentage of tasks that are overdue {str(round((z / len(tasks_dict)) * 100, 2))}%."
    # Now generating a 'task_overview' file.
    # The task_overview string is then written to the file in an easy to read format.
    f3 = open('task_overview.txt', 'w')
    f3.write(task_overview)
    # Setting variables to store information regarding total users, complete tasks for a user, incomplete tasks for the user,
    # incomplete and over-due tasks for the user respectively.


    f = open('user.txt', 'r')
    x = 0
    for i in f:
        x = x + 1
        names = i.split(',')
    user_overview = user_overview + "\n"
    user_overview = user_overview + f"The total number of users registered with task_manager.py is {x}."
    user_overview = user_overview + f"\nThe total number of tasks generated and tracked by task_manager.py is {str(len(tasks_dict))}."
    f.close()

    # Open the file in read mode
    text = open("tasks.txt", "r")
    # Create an empty dictionary
    my_dict = dict()
    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()[0:5]
        # Split the line into words
        words = line.split(" ", 1)
        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in my_dict:
                # Increment count of word by 1
                my_dict[word] = my_dict[word] + 1
            else:
                # Add the word to dictionary with count 1
                my_dict[word] = 1
    # Print the contents of dictionary
    for key in list(my_dict.keys()):
        user_overview = user_overview + f"\nThe total number of tasks assigned to {key} is {my_dict[key]}."
        user_overview = user_overview + f"\nThe percentage of the total number of tasks assigned to {key} is {str(round((my_dict[key] / len(tasks_dict)) * 100, 2))}%."
        user_overview = user_overview + "\n"

    b = 0
    c = 0
    d = 0
    for key in tasks_dict:
        # Checking for which tasks are complete by finding the 'Yes' string in each key of tasks_dict.
        if tasks_dict[key][0] == username and tasks_dict[key][5] == "Yes":  # Checking if the task for the user is complete.
            b += 1  # Integer 'b' is increased by 1 if the task is complete.
        elif tasks_dict[key][0] == username and tasks_dict[key][5] == "No":  # Checking if the task for the user is incomplete.
            c += 1  # Integer 'c' is increased by 1 if the task is incomplete.
            if over_due_check(tasks_dict[key][4]):  # Checking if the task is incomplete and overdue.
                d += 1  # If overdue, integer 'd' is increased by 1.
        user_overview = user_overview + f"\nThe percentage of tasks assigned to {tasks_dict[key][0]} that have been completed is {str(round((b / len(tasks_dict)) * 100, 2))}%."
        user_overview = user_overview + f"\nThe percentage of tasks still to be completed by {tasks_dict[key][0]} is {str(round((c / len(tasks_dict)) * 100, 2))}%."
        user_overview = user_overview + f"\nThe percentage of incomplete and overdue tasks assigned to {tasks_dict[key][0]} is {str(round((d / len(tasks_dict)) * 100, 2))}%."
        user_overview = user_overview + "\n"
            # Now generating a 'user_overview' file.
        # The user_overview string is then written to the file in an easy to read format.
        f4 = open('user_overview.txt', 'w')
        f4.write(user_overview)
    # The user then views a message stating that their reports have been successfully generated.
    # They do not have the option to view the reports.
    # The admin user can select to display statistics from their main menu.
    print("Your reports have been generated successfully.")

def task_editor():
    task_num = input("\nEnter just the number of the task you would like to edit or -1 to return to main menu: ")
    if task_num == '-1':
        print(user_choice)
    else:
        option = input("\nWould you like to mark the task as complete or edit the task? (e.g. mark OR edit): ").lower()
        if option == 'mark':
            tasks_dict[f"Task {task_num} details:"][5] = "Yes"
            print("Your task has been successfully marked as complete.")
            # If they choose to edit, the task must be incomplete/item in dictionary list equal to 'No'.
        elif option == "edit" and (tasks_dict[f"Task {task_num} details:"][5] == "No"):
            # They are given the option to edit username or due date.
            edit_choice = input("Would you like to edit the task username or dates? (Type 'U' or 'D'): ").lower()
            # If they choose to edit the username, they are prompted to enter a new username for the task.
            if edit_choice == "u":
                name_edit = input("Please enter a new username for the task: ")
                # The new name is assigned in the dictionary.
                tasks_dict[f"Task {task_num} details:"][0] = name_edit
                # Successful return message.
                print("The task username has been updated successfully.")
            # If they choose to edit the due date, they are prompted to enter a new date.
            elif edit_choice == "d":
                due_date_change = input("Please enter a new due date (e.g. 12 May 2020): ")
                # New date is updated in the tasks_dict.
                tasks_dict[f"Task {task_num} details:"][4] = due_date_change
                # Sucessful return message.
                print("The due date has been updated successfully.")
        elif option == "edit" and (tasks_dict[f"Task {task_num} details:"][5] == "Yes"):
            print("\nYou can only edit tasks that are not already complete. "
                    "\nChoose 'vm' from menu below to select another task to edit.")


# Checks the username and password logged in with and prints out all related tasks from tasks text file.
# Prints the username and tasks only
def view_mine():
    if user_choice == 'vm':
        f = open('tasks.txt', 'r')
        task_count = 0
        for key in tasks_dict:
            task_count += 1
            if username == (tasks_dict[key][0]):
                print(f"""------------------------------------------

        Task {str(task_count)}:      
        {str(tasks_dict[key][1])}
        Assigned to:        {str(tasks_dict[key][0])}
        Date assigned:      {str(tasks_dict[key][3])}
        Due Date:           {str(tasks_dict[key][4])}
        Task Complete?      {str(tasks_dict[key][5])}
        Task Description:
        {str(tasks_dict[key][2])}
         ---------------------------------------------------------""")
        task_editor()


print("Login below")

# The user and tasks details will be stored in corresponding dictionaries for use in the program.
user_details = {}
# Created empty lists for the usernames and passwords to be cast into
usernames_list = []
# Empty dictionary to store task information in
tasks_dict = {}

# Added a boolean variable for the loop
authorised = False
f = open('user.txt', 'r+')
for line in f:
    # Stripping newline characters from the line.
    newline = line.rstrip('\n')
    # Splitting the line into a list.
    split_line = newline.split(", ")
    # Assigning items from the list into corresponding list.
    usernames_list.append(split_line[0])
    # Lists are now stored as values assigned to keys in user_details dictionary.
    user_details["Usernames"] = usernames_list

count = 1
f2 = open("tasks.txt", 'r+')
for line in f2:
    newline = line.rstrip('\n')  # Stripping newline characters.
    split_line = newline.split(", ")  # Splitting line into a list of items.
    tasks_dict[f"Task {count} details:"] = split_line  # Assigning each list of items to a key in tasks_dict.
    count += 1  # Count used to change key value for each list of info.


# Loop for the username and password
# Strips the username and password into a list
while authorised != True:
    f = open('user.txt', 'r')
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    username = username.strip()
    password = password.strip()
    # Loop to check the user text file and strips the line and puts it in a list and new variable
    for i in f:
        loginInfo = i.strip().split(', ')
        # If statement that checks the username and password at index 0 and 1 in the new variable
        # Checks the username and password in the text file User.txt
        if username == loginInfo[0] and password == loginInfo[1]:
            authorised = True
    # If username and password match in usertxt file then print message
    if authorised:
        print("Username and Password correct! You have successfully logged in.")
    # If username and password do n0t match in usertxt file then print message
    elif username != True:
        print("Username and/or Password incorrect!")

    while authorised:
        if username == 'admin':
            user_choice = input("""\nPlease select one of the following options:

        r  - register user
        ds - display statistics
        gr - generate reports
        a  - add task
        va - view all tasks
        vm - view my tasks
        e  - exit

        : """).lower()
            print(user_choice)
            reg_user()
            generate_reports()
            display_stats()
            add_task()
            view_all()
            view_mine()
            # Breaks loop
            if user_choice == "e":
                break
        elif username != 'admin':
            user_choice = input("""\nPlease select one of the following options:

        a  - add task
        va - view all tasks
        vm - view my tasks
        e  - exit

        : """).lower()
            print(user_choice)
            add_task()
            view_all()
            view_mine()
            # Breaks loop
            if user_choice == "e":
                break