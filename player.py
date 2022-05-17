from deck import Deck


class Player:
    starting_money = 500
    bust = 22

    def __init__(self):
        self.money = Player.starting_money
        self.hand = []
        self.hand_value = 0
        self.current_bet = 0
        self.has_won = False

    def add_card_to_hand(self, new_card):
        self.hand.append(new_card)

    def update_hand_value(self):
        self.hand_value = self.check_hand_value()

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

    def decide_to_hit(self):
        choice = input('Would you like to hit or stay? ')
        choice = choice.strip().lower()
        if choice not in ['hit', 'stay']:
            print('That is not a valid option')
            self.decide_to_hit()
        if choice == 'hit':
            return True
        elif choice == 'stay':
            return False

    def make_bet(self):
        bet = input('Place your bet: ')
        if bet.isnumeric() is False:
            raise ValueError('Bet must be numeric')
        bet = float(bet)
        if bet < 1:
            print("Minimum bet is $1.")
            self.make_bet()
        elif bet > self.money:
            print("You cannot bet more money than you currently have.")
            self.make_bet()
        else:
            self.current_bet = bet

    def lose_bet(self):
        # Subtract your bet from your money pool, and set current bet to 0
        self.money -= self.current_bet

    def win_bet(self, multiplier=1):
        # Add winnings to your money pool, multiply if you win on opening hand
        winnings = round(self.current_bet * multiplier, 2)
        self.money += winnings
        self.has_won = True

    def end_round(self):
        self.current_bet = 0
        self.has_won = False



