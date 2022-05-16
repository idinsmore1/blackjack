import random


class Deck:
    possible_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = self._generate_deck()


    def _generate_deck(self):
        deck = []
        suits = [u"\u2666", u"\u2665", u"\u2663", u"\u2660"]
        for suit in suits:
            for val in Deck.possible_values:
                deck.append(f'{val}{suit}')
        random.shuffle(deck)
        return deck

    def deal_opening_hand(self):
        opening_hand = []
        for i in range(2):
            ix = random.randrange(len(self.cards))
            opening_hand.append(self.cards.pop(ix))
            random.shuffle(self.cards)
        return opening_hand