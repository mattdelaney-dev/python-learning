import random
import art

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1

    is_game_over = False

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def calculate_score(cards):
        """
        Takes a list of cards and calculates the score
        :param cards:
        :return:
        """
        if sum(cards) == 21 and len(cards) == 2:
            return 0

        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    def compare(u_score, c_score):
        if u_score == c_score:
            return "Draw"
        elif c_score == 0:
            return "You Lost!"
        elif u_score == 0:
            return "You Won!"
        elif u_score > 21:
            return "You Lost!"
        elif c_score > 21:
            return "You Won!"
        elif u_score > c_score:
            return "You Won!"
        else:
            return "You Lost!"

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to continue or 'n' to quit.")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack Type 'y' or 'n': ") == 'y':
    print('\n' * 20)
    play_game()