#=====importing libraries===========
print("---------------------------------")
'''This is the section where you will import libraries'''

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

valid_password = user_dict[username]
while True:
        password = input("Please enter your password: ")
        if password == valid_password:
              print("Login successful\n")
              break
        else:
                print("Password is incorrect...\n") 


while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : ''').lower()

    if menu == 'r':

        while True:
                new_user = input("please enter the new username: ")
                new_pass = input("please enter the new password for that user: ")
                confirm_pass = input("please confirm the new password: ")
                if confirm_pass == new_pass:
                    with open('user.txt', 'a') as f:
                        f.write(f"\n{new_user}, {new_pass}")
                        break
                else:
                    print("passwords did not match")
                    continue
        print(f"\n*** New user {new_user} succesfully registered! ***\n")
          
    
    
    elif menu == 'a':
        while True:
                username = input("please enter the name of the person who the task belongs to: ")
                if username in user_dict:
                    print("username is valid")
                    task_title = input("What is the name of the task?: ")
                    task_desc = input("What is the task description?: ").replace(',', '')
                    task_due = input("When is the task due?: ")
                    current_date = input("What is today's date?: ")
                    with open('tasks.txt', 'a') as f:
                                    f.write(f"\n{username}, {task_title}, {task_desc}, {current_date}, {task_due}, No")
                                            
                    break
                else:
                    print("username is not valid")


    elif menu == 'va':
    
        print("Here are all of the tasks:\n")
        with open("tasks.txt", "r") as file:
            for line in file:
                    line_split = line.strip("\n").split(", ")
                    print(f"\nTask: \t\t\t{line_split[1]} \nAssigned to: \t\t{line_split[0]} \nDate Assigned: \t\t{line_split[4]} \nDue Date: \t\t{line_split[3]} \nTask Complete?: \t{line_split[5]} \nTask Description: \t{line_split[2]}\n")



    elif menu == 'vm':
        print("\nHere are your tasks!")
        with open("tasks.txt", "r") as file:
            for line in file:
                    line_split = line.strip("\n").split(", ")
                    if line_split[0] == username:
                        print(f"\nTask: \t\t\t{line_split[1]} \nAssigned to: \t\t{line_split[0]} \nDate Assigned: \t\t{line_split[4]} \nDue Date: \t\t{line_split[3]} \nTask Complete?: \t{line_split[5]} \nTask Description: \t{line_split[2]}\n")
        print("...end of your task list\n")

    elif menu == 'e':
        print('Goodbye!!!\n\n')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")