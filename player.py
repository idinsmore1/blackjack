from deck import Deck

class Player:
    starting_money = 500
    face_card_val = 10
    card_values = {}
    for suit in Deck.suits:
        for val in Deck.numeric_values:
            card_values[f'{val}{suit}'] = val
        for face in ['J', 'Q', 'K']:
            card_values[f'{val}{suit}'] = 10
        card_values[f'A{suit}'] = 1

    def __init__(self, type):
        self.type = type
        self.money = Player.starting_money
        self.hand = None
        self.hand_value = None

    def check_hand_value(self):
        card_vals = []
        for card in self.hand:
            print(card)



