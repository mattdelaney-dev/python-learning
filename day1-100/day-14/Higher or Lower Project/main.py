import game_data
import art
import random
def random_person():
    return random.choice(game_data.data)

def display_person(person):
    p_name = person['name']
    p_description = person['description']
    p_country = person['country']
    return f"{p_name}, {p_description}, {p_country}"

def compare_person(a, b, user_input):
    a_followers = a['follower_count']
    b_followers = b['follower_count']
    guess = user_input
    if guess == "A":
        if a_followers > b_followers:
            return True
        else:
            return False
    elif guess == "B":
        if b_followers > a_followers:
            return True
        else:
            return False
    else:
        print("Invalid input")
        return False



def game():
    game_over = True
    person_a = random_person()
    score = 0

    while game_over:
        print("\n" * 20)
        print(art.logo)
        person_b = random_person()
        while person_b == person_a:
            person_b = random_person()
        print(f"Compare A: {display_person(person_a)}")
        print(art.vs)
        print(f"Compare B: {display_person(person_b)}")
        guess_input = input("Who has more followers? Type 'A' or 'B'.").upper()
        if compare_person(person_a, person_b, guess_input):
            score += 1
            person_a = person_b
        else:
            game_over = False


    print(f"Final score: {score}")

game()