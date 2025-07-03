import art
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def random_card_pick():
    """
        Rastgele bir kart ceker.
    """
    return random.choice(cards)

def calculate_score(cards_in_hand):
    """
        Eldeki kartlardan toplam skoru hesaplar.
        Eger elinde 11 varsa onun 1 veya 11 sayılacağını da hesap eder.
    """
    while True:
        total = sum(cards_in_hand)

        if total > 21:
           if 11 in cards_in_hand:
               index = cards_in_hand.index(11)
               cards_in_hand[index] = 1
           else:
               return total
        else:
            return total

def play_computer(computer_cards):
    """
        Bilgisayarin oyunu oynamasini saglar.
        Eger eli 17'den kucukse kart ceker.
    """

    play = True
    while play:
        score = calculate_score(computer_cards)

        if score < 17:
            computer_cards.append(random_card_pick())
        else:
            play = False


keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
keep_playing_check = True

if keep_playing == "n":
    keep_playing_check = False

while keep_playing_check:
    print(art.logo)

    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0

    user_cards.append(random_card_pick())
    computer_cards.append(random_card_pick())

    get_another_card_check = True
    while get_another_card_check:

        user_cards.append(random_card_pick())
        user_score = calculate_score(user_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score >= 21:
            get_another_card_check = False
        else:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass:")
            if get_another_card == "n":
                get_another_card_check = False

    print(f"  Your final hand: {user_cards}, final score: {user_score}")

    if user_score == 21 and len(user_cards) == 2:
        computer_cards.append(random_card_pick())
    elif user_score <= 21:
        play_computer(computer_cards)
    computer_score = calculate_score(computer_cards)

    print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")

    if user_score > 21:
        print("You went over. You lose 😭")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif user_score == 21 and len(user_cards) == 2 and (len(computer_cards) != 2 or computer_score != 21):
        print("Win with a Blackjack 😎")
    elif computer_score == 21 and len(computer_cards) == 2 and (len(user_cards) != 2 or user_score != 21):
        print("Lose, opponent has Blackjack 😱")
    elif user_score > computer_score:
        print("You win 😃")
    elif user_score < computer_score:
        print("You lose 😤")
    else:
        print("Draw 🙃")

    keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if keep_playing == "n":
        keep_playing_check = False
    else:
        print("\n" * 30)

print("Goodbye :)")
