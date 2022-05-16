from random import shuffle


class Deck:

    def __init__(self):
        self.cards = self._generate_deck()


    def _generate_deck(self):
        deck = []
        suits = [u"\u2666", u"\u2665", u"\u2663", u"\u2660"]
        for suit in suits:
            for i in range(2, 11):
                deck.append(f'{i}{suit}')
            for face in ['A', 'K', 'Q', 'J']:
                deck.append((f'{face}{suit}'))
        shuffle(deck)
        return deck