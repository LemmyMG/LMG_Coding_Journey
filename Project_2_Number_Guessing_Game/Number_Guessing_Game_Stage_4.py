# Store the secret number
secret_number = 7

# Ask the user for a number, convert their answer into an integer,
# and store that integer in guess
guess = int(input("Guess the number: "))

# Compare the guess with the secret number
if guess == secret_number:
    print("Correct! You guessed the number.")
elif guess > secret_number:
    print("Too high!")
else:
    print("Too low!")