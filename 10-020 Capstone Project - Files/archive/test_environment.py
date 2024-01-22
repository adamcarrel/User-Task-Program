with open("user.txt", "r") as file:
        data = file.readlines()

user_dict = {}
for entry in data:
        # remove the newline
        # split up username + password
        # add to dictionary
        entry_split = entry.strip("\n").split(", ")
        user_dict[entry_split[0]] = entry_split[1]

print(user_dict)
# Login
# verify username
# verify password
# Do we have a known range?
# verify via the dict
while True:
        username = input("Please enter username: ")
        if username in user_dict.keys():
              print("Username valid")
              break
        else:
                print("Credentials did not match")

valid_password = user_dict[username]
while True:
        password = input("Please enter your password: ")
        if password == valid_password:
              print("Login successful")
              break
        else:
                print("Credentials did not match")