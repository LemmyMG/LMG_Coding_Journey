import random


# Keep the game running until the player chooses to stop
while True:
    # Generate a new secret number for each round
    secret_number = random.randint(1, 10)

    # Give the player only 3 guesses
    attempts_left = 3

    print("\nI'm thinking of a number between 1 and 10.")

    # Keep asking for guesses while attempts remain
    while attempts_left > 0:
        try:
            guess = int(input("\nGuess the number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Reduce attempts after a valid guess
        attempts_left -= 1

        # Compare the guess with the secret number
        if guess == secret_number:
            print("Correct! You guessed the number.")
            break

        elif guess > secret_number:
            print(f"Too high! You have {attempts_left} attempt(s) left.")

        else:
            print(f"Too low! You have {attempts_left} attempt(s) left.")

    else:
        print(f"\nYou are out of attempts. The number was {secret_number}.")

    # Ask whether the player wants another round
    while True:
        answer = input("\nPlay another round? (yes/no): ").strip().lower()

        if answer == "yes":
            break

        elif answer == "no":
            break

        else:
            print("Please enter yes or no.")

    # Exit the main game loop if the player chooses no
    if answer == "no":
        break


print("\nGame over!")
