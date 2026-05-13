import art
import random
print(art.logo)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_guess(u_guess, r_number, turns):
    if u_guess > r_number:
        print("Too high.")
        return turns -1
    elif u_guess < r_number:
        print("Too low.")
        return turns -1
    else:
        print(f"You guessed {r_number} correctly.")
        return "You Win!"

def check_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1,101)
    print(f"Pssst, the correct answer is {random_number}.")

    turns = check_difficulty()

    guess = 0

    while guess != random_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_guess(guess, random_number, turns)
        if turns == 0:
            print("You lose.")
            return
        elif guess != guess:
            print("Guess again!")

game()