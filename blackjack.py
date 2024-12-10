import random
import art
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score,c_score):
    if u_score==c_score:
        return " its a draw"
    elif c_score==0:
        return "you loose"
    elif u_score==0:
        return "you win"
    elif u_score>21:
        return "you loose"
    elif c_score>21:
        return "you win"
    elif u_score>c_score:
        return "you win"
    else:
        return "you loose"
def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    user_score=-1
    computer_score=-1
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_not_over =False
    while not game_not_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score((computer_cards))
        print(f"your cards are {user_cards} and there sum is {user_score}")
        print(f"computers first card is {computer_cards[0]}")
        if user_score==0 or  computer_score==0 or user_score>21:
            game_not_over=True
        else:
            should_draw_new_card=input("type 'y' if you want to draw new card and type'n' if you don't want to draw the card\n").lower()
            if should_draw_new_card=="y":
                user_cards.append(deal_card())
            else:
                game_not_over=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score((computer_cards))

    print (f"your final cards are {user_cards}and your total is  {user_score}")
    print (f"computers final cards are {computer_cards}and your total is  {computer_score}")
    print(compare(user_score,computer_score))

while input("do you want to play game of blackjack. type 'y' for yes or 'n' for no\n") =="y":
    print("\n"*20)
    play_game()