import random


class Deck:
    numeric_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
    face_values = ['J', 'Q', 'K', 'A']
    suits = [u"\u2666", u"\u2665", u"\u2663", u"\u2660"]
    card_values = {}
    for suit in suits:
        for val in numeric_values:
            card_values[f'{val}{suit}'] = int(val)
        for face in ['J', 'Q', 'K']:
            card_values[f'{face}{suit}'] = 10
        card_values[f'A{suit}'] = 11

    def __init__(self):
        self.cards = Deck.generate_deck()

    @classmethod
    def generate_deck(self):
        deck = []
        for suit in Deck.suits:
            for val in Deck.numeric_values:
                deck.append(f'{val}{suit}')
            for val in Deck.face_values:
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

    def hit(self):
        return self.cards.pop(random.randrange(len(self.cards)))

    def start_new_round(self):
        self.cards = Deck.generate_deck()
