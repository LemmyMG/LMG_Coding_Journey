# Store the credentials used for validation
correct_username = "admin"
correct_password = "1234"
# Track the number of login attempts made by the user
attempts = 0
# Define the maximum number of login attempts allowed
max_attempts = 3
login_successful = False

while attempts < max_attempts:
    # Collect login credentials from the user
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Count this login submission as an attempt
    attempts += 1
    print(f"Attempt: {attempts}")

    # Check whether both credentials are correct
    if username == correct_username and password == correct_password:
        print("Login successful.")
        login_successful = True
        break
    else:
        print("Invalid credentials.")

# Lock the account when the maximum number of attempts is reached
if not login_successful:
    print(f"Maximum allowed attempts: {max_attempts}.")
    print("Account locked.")