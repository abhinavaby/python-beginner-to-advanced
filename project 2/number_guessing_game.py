import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

guesses = 0

print("Welcome to The Perfect Guess Game!")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    guesses += 1

    if guess > number:
        print("Lower number please!")
    elif guess < number:
        print("Higher number please!")
    else:
        print(f"\nCongratulations! You guessed the number {number}.")
        print(f"You took {guesses} guesses.")
        break