# Store the credentials used for validation
correct_username = "admin"
correct_password = "1234"

attempts = 0

while True:
    # Collect login credentials from the user
    username = input("Enter username: ")
    password = input("Enter password: ")

    attempts += 1
    print(f"Attempt: {attempts}")
    # Login succeeds only when both credentials match
    if username == correct_username and password == correct_password:
        print("Login successful.")
        break
    else:
        print("Invalid credentials")
       