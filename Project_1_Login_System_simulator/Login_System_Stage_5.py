# Store the credentials used for validation
correct_username = "admin"
correct_password = "1234"

# Track the number of login attempts made by the user
attempts = 0

# Define the maximum number of login attempts allowed
max_attempts = 4

while True:
    # Collect login credentials from the user
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Count this login submission as an attempt
    attempts += 1
    print(f"Attempt: {attempts}")

    # Check whether both credentials are correct
    if username == correct_username and password == correct_password:
        print("Login successful.")
        break

    # Lock the account when the maximum number of attempts is reached
    elif attempts >= max_attempts:
        print("Invalid credentials.")
        print(f"Maximum allowed attempts: {max_attempts}.")
        print("Account locked.")
        break

    # Allow another attempt when the limit has not been reached
    else:
        print("Invalid credentials.")