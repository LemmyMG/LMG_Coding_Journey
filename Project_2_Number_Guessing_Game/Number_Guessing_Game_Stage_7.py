import random

def play_game(starting_attempts):
    # Outer loop controls overall game sessions (replayability)
    while True:
        secret_number = random.randint(1, 10)
        
        # Initialize attempt limit using the function argument
        attempts_left = starting_attempts

        print("\nI'm thinking of a number between 1 and 10.")

        # Inner loop handles guess processing for a single round
        while attempts_left > 0:
            # Input validation: prevents invalid entries (like letters) from crashing the program
            try:
                guess = int(input("\nGuess the number: "))
            except ValueError:
                print("Please enter a valid number.")
                continue  # Skip to next loop iteration without losing an attempt

            attempts_left -= 1

            if guess == secret_number:
                print("Correct! You guessed the number.")
                break  # Exit inner loop early on victory

            elif guess > secret_number:
                print(f"Too high! You have {attempts_left} attempt(s) left.")
            else:
                print(f"Too low! You have {attempts_left} attempt(s) left.")

        # Executed ONLY if the inner loop finishes naturally (attempts hit 0 without a 'break')
        else:
            print(f"\nYou are out of attempts. The number was {secret_number}.")

        # Replay validation loop: forces user to input a valid response before moving on
        while True:
            answer = input("\nPlay another round? (yes/no): ").replace(" ","").strip().lower()

            if answer in ("yes", "no"):
                break
            print("Please enter yes or no.")

        # Break outer game loop if player selects 'no'
        if answer == "no":
            break

    return "\nGame over!"

result = play_game(4)
print(result)
