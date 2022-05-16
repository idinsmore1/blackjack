from deck import Deck


class Player:
    starting_money = 500
    bust = 22

    def __init__(self):
        self.money = Player.starting_money
        self.hand = []
        self.hand_value = 0
        self.current_bet = None

    def check_hand_value(self):
        card_vals = []
        for card in self.hand:
            card_vals.append(Deck.card_values[card])
        current_sum = sum(card_vals)
        while current_sum > Player.bust and any(11 == c for c in card_vals):
            for index, val in enumerate(card_vals):
                if val == 11:
                    card_vals[index] = 1
                    current_sum = sum(card_vals)
                    break
        return current_sum

    def make_bet(self, bet):
        self.current_bet = bet
        self.money = self.money - bet


