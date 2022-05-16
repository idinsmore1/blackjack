from random import shuffle


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
        shuffle(deck)
        return deck

    def deal(self):
        pass