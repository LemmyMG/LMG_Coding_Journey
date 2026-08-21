#Store the secret number
secret_number = 7

# Ask the user for a number, convert their answer into an integer, and store that integer in guess
guess = int(input("Guess the number: "))

# Compare guess number to secret mumber
if guess == secret_number:
    print("Correct! You guessed the number.")
