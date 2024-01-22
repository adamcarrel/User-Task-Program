#=====importing libraries===========
print("---------------------------------")
'''This is the section where you will import libraries'''

# defining the functions for the user menu

def reg_new_user():
     while True:
        new_user = input("please enter the new username: ")
        new_pass = input("please enter the new password for that user: ")
        confirm_pass = input("please confirm the new password: ")
        if confirm_pass == new_pass:
            with open('user.txt', 'a') as f:
                f.write(f"\n{new_user}, {new_pass}")
                print(f"\n*** New user {new_user} succesfully registered! ***\n")
                break
        else:
            print("passwords did not match")
            continue

def view_all():
    print("Here are all of the tasks:\n")
    with open("tasks.txt", "r") as file:
                    for line in file:
                        try:
                            line_split = line.strip("\n").split(", ")
                            print(f"\nTask: \t\t\t{line_split[1]}\nAssigned to: \t\t{line_split[0]} \nDate Assigned: \t\t{line_split[3]} \nDue Date: \t\t{line_split[4]} \nTask Complete?: \t{line_split[5]} \nTask Description: \t{line_split[2]}\n")
                        except Exception: # as discussed in feedback. I have used this to deal with
                            continue      # any blank lines that appear. I have left a blank line on tasks.txt to demonstrate 
                                      
def view_my(username):
    print("\nHere are your tasks!")
    with open("tasks.txt", "r") as file:
        for line in file:
                line_split = line.strip("\n").split(", ")
                if line_split[0] == username:
                    print(f"\nTask: \t\t\t{line_split[1]} \nAssigned to: \t\t{line_split[0]} \nDate Assigned: \t\t{line_split[3]} \nDue Date: \t\t{line_split[4]} \nTask Complete?: \t{line_split[5]} \nTask Description: \t{line_split[2]}\n")
    print("...end of your task list\n")

def add_task():
      while True:
                username = input("please enter the name of the person who the task belongs to: ")
                if username in user_dict:
                    print("username is valid")
                    task_title = input("What is the name of the task?: ")
                    task_desc = input("What is the task description?: ").replace(',', '')
                    task_due = input("When is the task due?: ")
                    with open('tasks.txt', 'a') as f:
                                    f.write(f"\n{username}, {task_title}, {task_desc}, {(today.strftime('%d %b %Y'))}, {task_due}, No")
                                            
                    break
                else:
                    print("username is not valid")
      
def statistics():
    print("\nStatistics:\n")
      # Googled a simple piece of code for counting lines in a text file. I am aware I could have used
      #readlines - 
        # https://pynative.com/python-count-number-of-lines-in-file/#:~:text=Use%20readlines()%20to%20g
        # et%20Line%20Count,-If%20your%20file&text=This%20is%20the%20most%20straightforward,lines%20pre
        # sent%20in%20a%20file.
    with open(r"tasks.txt", 'r') as file:
                for count, line in enumerate(file):
                    pass #I'm not totally sure why this pass code is used here
    print('Number of tasks: \t', count + 1)

    with open(r"user.txt", 'r') as file:
                for count, line in enumerate(file):
                    pass
    print('Number of users: \t', count + 1)
    print("\n")
        

# importing datetime module for use with tasks, as discussed in feedback
from datetime import date
today = date.today()


# using readlines to create a dictionary from user.txt
with open("user.txt", "r") as file:
        data = file.readlines()

user_dict = {}
for entry in data:
        # remove the newline
        # split up username + password
        # add to dictionary
        entry_split = entry.strip("\n").split(", ")
        user_dict[entry_split[0]] = entry_split[1]

#====Login Section====
print("__̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡̡̡̡.___\n")# ASCII art for decoration!

print("Welcome to the staff task program!\n")

# While loop that checks if the username is in the dictionary
while True:
        username = input("Please enter username: ").strip().lower()
        if username in user_dict.keys():
              print("Username valid")
              break
        else:
                print("No such user exists...")

# create a variable valid_password that reads the value of the relevant key
valid_password = user_dict[username]

# While loop to validate password 
while True:
        password = input("Please enter your password: ")
        if password == valid_password:
              print("Login successful\n")
              break
        else:
                print("Password is incorrect...\n") 

# User menu section----------------------------------------

while True:
    # I have defined functions for each menu option, other than exit

    menu = input('''Select one of the following options:
    r - register a user (admin only)
    a - add task
    va - view all tasks
    vm - view my tasks
    s - statistics (admin only)
    e - exit
    : ''').lower()

    if menu == 'r' and username != "admin":# error message for non admin users
        print("\nSorry, this feature is for administrators only.\n")

    # most menu entries result in the relevant function being called
    elif menu == 'r':
          reg_new_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()
                    
    elif menu == 'vm':
       view_my(username)

    # checking if user is allowed to access statistics
    elif menu == 's' and username != "admin":
        print("Sorry, statistics is for administrators only.\n")

    elif menu == 's':
        statistics()

    elif menu == 'e':
        print('Goodbye!!!\n\n')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")