# correct_username = "admin"
# correct_password = "1234"

# max_attempts = 3
# attempt = 0
# logged_in = False

# while attempt < max_attempts:
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     attempt += 1
#     print(f"Attempt: {attempt}")

#     if username == correct_username and password == correct_password:
#         print("Login successful.")
#         logged_in = True
#         break
#     else: 
#         print("Invalid name or passowrd.")
        
# if not logged_in:
#     print(f"Account locked. maximum  {attempt} attempts reached.")



correct_username = "admin"
correct_password = "1234"

max_attempts = 4
attempts = 0

while attempts < max_attempts:

    username = input("Enter username: ")

    if username != correct_username:

        print("Incorrect username. Try again.")
        attempts += 1
        continue

    elif username == correct_username:
        break

while attempts < max_attempts:

    password = input("Enter password: ")

    if password != correct_password:

        print("Incorrect password. Try again. ")
        attempts += 1
        continue

    elif password == correct_password:

        print("Login successful!")
        break

    else:
        print("Account locked.")