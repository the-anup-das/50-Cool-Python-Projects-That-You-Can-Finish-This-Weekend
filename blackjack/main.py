logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


print(logo)

#jack/queen/king all count as 10
#ace can be 1 or 11 initially taking ace value as 11

import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    #blackjack
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    #ace value calculate
    #A+K+Q = 11+10+10 =31 that time A value will be 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def game_login(user_score, computer_score):
    if user_score > 21:
        return "You went over. You lose 😤"
    elif computer_score > 21:
        return "Opponet went over. You win 😁"
    elif user_score == computer_score:
        return "Draw 🙃"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif computer_score == 0:
        return "Lose! oppenent win with a Blackjack 😱"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play():
    user_cards = []
    computer_cards = []
    FLAG_GAME_OVER = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not FLAG_GAME_OVER:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
#        print(f"Computer cards: {computer_cards}, current score: {computer_score}")
        print(f"Computer first hand: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            FLAG_GAME_OVER = True 
        elif user_score == 21 or computer_score == 21:
            FLAG_GAME_OVER =True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                FLAG_GAME_OVER = True

    while computer_score != 0 and computer_score < 18:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"You final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(game_login(user_score,computer_score))

user_reponse = "y"
while user_reponse == "y":
    play()
    user_reponse = input("Do you want to play again a game of Blackjack? Type 'y' for yes or 'n' for no:").lower()