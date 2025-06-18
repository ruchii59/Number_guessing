import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0  # Make sure this line is inside the function

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1  # Now this works because 'attempts' is defined

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Call the function to start the game
number_guessing_game()


