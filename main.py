from deck import Deck

if __name__ == '__main__':
    deck = Deck()
    print(len(deck.cards))
    player_hand = deck.deal_opening_hand()
    dealer_hand = deck.deal_opening_hand()
    print(player_hand, dealer_hand, len(deck.cards))

