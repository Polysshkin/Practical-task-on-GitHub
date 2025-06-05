import random


def guess_the_number():
    secret = random.randint(1, 100)
    attempts = 7

    print("Guess the number between 1 and 100.")

    for i in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {i}/{attempts}: "))
        except ValueError:
            print("Invalid input. Enter an integer.")
            continue

        if guess == secret:
            print(
                f"Congratulations! You guessed the number {secret} "
                f"in {i} attempt(s)."
            )
            return
        elif guess < secret:
            print("Too low.")
        else:
            print("Too high.")

    print(f"Game over. The number was {secret}.")


guess_the_number()
