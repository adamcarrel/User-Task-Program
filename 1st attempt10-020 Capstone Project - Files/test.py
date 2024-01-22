# #creating a dictionary by reading lines from user.txt
# # my_dict = {}

# # with open("user.txt", 'r') as f:
# #     for line in f:
# #         x = (line.replace(",", ""))
# #         print(x) #checking my output
# #         items = x.split()
# #         key, values = items[0], items[1:]
# #         my_dict[key] = values

# # #sanity check
# # print(my_dict)
# # print(f"the password for john's account is {my_dict['john']}")

# # answer_1 = "john"
# # answer_2 = "panther"
# # getin_1 = input("Enter your Username: ")
# # getin_2 = input("Enter your password: ")


# # while getin_1 != answer_1 or getin_2 != answer_2:
# #     print("Incorrect")
# #     print("Please proceed")
# #     getin_1 = input("Enter your Username: ")
# #     getin_2 = input("Enter your password: ")

# # print("Your username and password are OK.")   

# # new_user = input("please enter the new username: ")
# # new_pass = input("please enter the new password for that user: ")


# # while True:
# #         confirm_pass = input("please confirm the new password: ")
# #         if confirm_pass == new_pass:
# #             with open('user.txt', 'a') as f:
# #                 f.write(f"\n{new_user}, {new_pass}")
# #                 break
# #         else:
# #             print("passwords did not match")

# print("++++++++++++++++++++")
# with open("user.txt", "r") as file:
#         data = file.readlines()

# user_dict = {}

# for entry in data:
#         # remove the newline
#         # split up username + password
#         # add to dictionary
#         entry_split = entry.strip("\n").split(", ")
#         user_dict[entry_split[0]] = entry_split[1]


# # add to tasks



# # while True:
# #     username = input("please enter the name of the person who the task belongs to: ")
# #     if username in user_dict:
# #         print("username is valid")
# #         task_title = input("What is the name of the task?: ")
# #         task_desc = input("What is the task description?: ")
# #         task_due = input("When is the task due?: ")
# #         current_date = input("What is today's date?: ")
# #         with open('tasks.txt', 'a') as f:
# #                         f.write(f"\n{username}, {task_title}, {task_desc}, {current_date}, {task_due}, No")
                                
# #         break
# #     else:
# #         print("username is not valid")
        

    
# # with open("tasks.txt", "r") as file:
# #        for line in file:
# #                line_split = line.strip("\n").split(", ")
# #             #    print("User/Task/Description/Due Date/Current Date/Completed? ")
# #                print(f"\nUser: {line_split[0]} \nTask: {line_split[1]} \nTask Description: {line_split[2]} \nDue Date: {line_split[3]} \nToday's Date: {line_split[4]} \nCompleted?: {line_split[5]}")


# with open("tasks.txt", "r") as file:
#        username = input("whats user name?: ")
#        for line in file:
#             line_split = line.strip("\n").split(", ")
#             # print(line_split[0] + "!")
#             if line_split[0] == username:
#                    print("\nIt's a match!\n")
#                    print(f"\nUser: {line_split[0]} \nTask: {line_split[1]} \nTask Description: {line_split[2]} \nDue Date: {line_split[3]} \nToday's Date: {line_split[4]} \nCompleted?: {line_split[5]}")

# Googled a simple piece of code for counting lines in a text file:
# https://pynative.com/python-count-number-of-lines-in-file/#:~:text=Use%20readlines()%20to%20g
# et%20Line%20Count,-If%20your%20file&text=This%20is%20the%20most%20straightforward,lines%20pre
# sent%20in%20a%20file.
with open(r"tasks.txt", 'r') as file:
            for count, line in enumerate(file):
                pass
print('Number of tasks: \t', count + 1)


# print("***********************")