import numpy as np
from deck import Deck

class Player:
    starting_money = 500
    face_card_val = 10
    card_values = {}
    bust = 22
    for suit in Deck.suits:
        for val in Deck.numeric_values:
            card_values[f'{val}{suit}'] = int(val)
        for face in ['J', 'Q', 'K']:
            card_values[f'{face}{suit}'] = 10
        card_values[f'A{suit}'] = 11

    def __init__(self, type):
        self.type = type
        self.money = Player.starting_money
        self.hand = []
        self.hand_value = None

    def check_hand_value(self):
        card_vals = []
        for card in self.hand:
                card_vals.append(Player.card_values[card])
        current_sum = sum(card_vals)
        print(current_sum, card_vals)
        while current_sum > Player.bust and any(11 == c for c in card_vals):
            for index, val in enumerate(card_vals):
                if val == 11:
                    card_vals[index] = 1
                    current_sum = sum(card_vals)
                    break
        return current_sum



