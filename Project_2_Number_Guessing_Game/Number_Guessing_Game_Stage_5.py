# Store the secret number
secret_number = 7

# Give guess an initial value so the loop has a value to compare
guess = 0

# Keep asking for guesses until the user guesses the secret number
while guess != secret_number:

    # Ask the user for a number, convert their answer into an integer,
    # and store that integer in guess
    guess = int(input("Guess the number: "))

    # # Compare the guess with the secret number and give feedback
    if guess == secret_number:
        print("Correct! You guessed the number.")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Too low!")