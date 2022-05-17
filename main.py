from deck import Deck
from player import Player


def ask_to_play(player):
    want_to_play = input(f'You are starting with {player.money}. Would you like to play a hand? ')
    want_to_play = want_to_play.strip().lower()
    # Check to see if it's a yes or no answer
    if want_to_play not in ['yes', 'no']:
        print('That is not a valid option.')
        ask_to_play(player)
    # if the player does not want to continue, exit the program
    if want_to_play == 'no':
        print('Thanks for playing!')
        exit()
    else:
        return


if __name__ == '__main__':
    player = Player()
    dealer = Player()
    deck = Deck()
    BLACKJACK = 21
    print("Welcome to Blackjack!")
    while player.money >= 1:
        # ask the player if they want to play
        ask_to_play(player)
        deck.start_new_round()
        # if they do want to play, have them place a bet
        player.make_bet()
        # Deal player opening hand
        player.hand = deck.deal_opening_hand()
        print(f'You are dealt {", ".join(player.hand)}')
        player.update_hand_value()
        # Deal dealer opening hand
        dealer.hand = deck.deal_opening_hand()
        dealer.update_hand_value()
        print(f'The dealer is dealt: {dealer.hand[0]}, unknown')
        if player.hand_value == BLACKJACK:
            print(f'The dealer has {", ".join(dealer.hand)}')
            if dealer.hand_value != BLACKJACK:
                print(f'Blackjack! You win ${round(player.current_bet * 1.5, 2)} :)')
                player.win_bet(1.5)
            else:
                assert player.hand_value == dealer.hand_value
                print('You tie. Your bet has been returned.')
        if dealer.hand_value == BLACKJACK and player.hand != BLACKJACK:
            print(f'The dealer wins, you lose ${player.current_bet} :(')
            player.lose_bet()
            dealer.win_bet()

        if player.has_won is False and dealer.has_won is False:
            # Player turn
            while True:
                hit = player.decide_to_hit()
                if hit:
                    new_card = deck.hit()
                    print(f'You are dealt: {new_card}')
                    player.add_card_to_hand(new_card)
                    print(f'You now have {", ".join(player.hand)}')
                    player.update_hand_value()
                    if player.hand_value > Player.bust:
                        print(f'Your hand value is over 21 and you lose {player.current_bet} :(')
                        player.lose_bet()
                        dealer.win_bet()
                        break
                    elif player.hand_value == BLACKJACK:
                        print(f"Blackjack! You win {player.current_bet}! :)")
                        player.win_bet()
                        break
                else:
                    break

            if player.has_won is False:
                # Dealer Turn
                print(f'The dealer has: {", ".join(dealer.hand)}')
                while True:
                    if dealer.hand_value < 17:
                        new_card = deck.hit()
                        print(f'The dealer hits and is dealt: {new_card}')
                        dealer.add_card_to_hand(new_card)
                        print(f'The dealer has: {", ".join(dealer.hand)}')
                        dealer.update_hand_value()
                        if dealer.hand_value >= Player.bust:
                            print(f"The dealer busts, you win {player.current_bet}! :)")
                            player.win_bet()
                            break
                        elif dealer.hand_value == BLACKJACK:
                            print(f"Dealer has Blackjack, you lose {player.current_bet}")
                            player.lose_bet()
                            dealer.win_bet()
                            break
                    else:
                        print('The dealer stays.')
                        break

        if player.has_won is False and dealer.has_won is False:
            if player.hand_value > dealer.hand_value:
                print(f"You win! You've won {player.current_bet}!")
                player.win_bet()
                dealer.lose_bet()
            elif player.hand_value < dealer.hand_value:
                print(f"The dealer wins. You lost {player.current_bet}.")
                player.lose_bet()
                dealer.win_bet()
            else:
                print("You tied. Your bet is returned to you.")
        player.end_round()
        dealer.end_round()




    print("You've ran out of money. Please restart this program to try again. Goodbye.")
    exit()

