from deck import Deck
from player import Player

if __name__ == '__main__':
    deck = Deck()
    player = Player('player')
    # dealer = Player('dealer')
    player.hand = deck.deal_opening_hand()
    # dealer.hand = deck.deal_opening_hand()
    player.hand.append('A♥')
    # player.hand.append('A♥')
    print(player.hand, len(deck.cards))
    print(player.check_hand_value())

