# Store the credentials used for validation
correct_username = "admin"
correct_password = "1234"

# Track the number of login attempts
attempts = 0

# Set the maximum number of failed attempts allowed
max_attempts = 4

while True:
    # Collect login credentials from the user
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Increase the attempt counter after each login submission
    attempts += 1
    print(f"Attempt: {attempts}")

    # Login succeeds only when both credentials match
    if username == correct_username and password == correct_password:
        print("Login successful.")
        break

    # Lock the account after the maximum number of attempts
    elif attempts >= max_attempts:
        print("Account locked.")
        break

    # Continue allowing login attempts while the limit has not been reached
    else:
        print("Invalid credentials.")