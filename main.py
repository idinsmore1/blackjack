from deck import Deck
from player import Player

def place_bet(current_money):
    bet = int(input('Place your bet: '))
    if bet < 1:
        print("Minimum bet is $1.")
        place_bet(current_money)
    elif bet > current_money:
        print("You cannot bet more money than you currently have.")
        place_bet(current_money)
    else:
        return bet


if __name__ == '__main__':
    player = Player()
    dealer = Player()
    deck = Deck()
    print("Welcome to Blackjack!")
    while player.money >= 1:
        want_to_play = input(f'You are starting with {player.money}. Would you like to play a hand? ')
        if want_to_play.strip().lower() == 'no':
            print('Thanks for playing!')
            break

        bet = place_bet(player.money)
        player.make_bet(bet)
        print(player.current_bet, player.money)
        player.hand = deck.deal_opening_hand()
        # dealer.hand = deck.deal_opening_hand()
        # player.hand.append('A♥')
        # print(player.hand, len(deck.cards))
        print(player.check_hand_value())

    print("You've ran out of money. Please restart this program to try again. Goodbye.")

