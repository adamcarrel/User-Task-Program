def view_my(username):
    print("\nHere are your tasks!")
    with open("tasks.txt", "r") as file:
        for line in file:
                line_split = line.strip("\n").split(", ")
                if line_split[0] == username:
                    print(f"\nTask: \t\t\t{line_split[1]} \nAssigned to: \t\t{line_split[0]} \nDate Assigned: \t\t{line_split[3]} \nDue Date: \t\t{line_split[4]} \nTask Complete?: \t{line_split[5]} \nTask Description: \t{line_split[2]}\n")
    print("...end of your task list\n")

# defining view_all
def view_all():
    print("Here are all of the tasks:\n")
    with open("tasks.txt", "r") as file:
        for line in file:
                line_split = line.strip("\n").split(", ")
                print(f"\nTask: \t\t\t{line_split[1]} \nAssigned to: \t\t{line_split[0]} \nDate Assigned: \t\t{line_split[3]} \nDue Date: \t\t{line_split[4]} \nTask Complete?: \t{line_split[5]} \nTask Description: \t{line_split[2]}\n")

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

username = input("what's your username?: ")
def add_task():
    while True:
                username = input("please enter the name of the person who the task belongs to: ")
                if username in user_dict:
                    print("username is valid")
                    task_title = input("What is the name of the task?: ")
                    task_desc = input("What is the task description?: ").replace(',', '')
                    task_due = input("When is the task due?: ")
                    with open('tasks.txt', 'a') as f:
                                    f.write(f"\n{username}, {task_title}, {task_desc}, {(today.strftime('%d/%m/%Y'))}, {task_due}, No")
                                            
                    break
                else:
                    print("username is not valid")
# view_my(username)
# view_all()
# reg_new_user()
add_task()