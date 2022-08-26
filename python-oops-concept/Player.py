from random import randint

class Player:

    def __init__(self, num_players):
        self.num_players = num_players
        self.score = 0

    def make_move(self):
        roll = randint(1, 6)
        self.score += roll
        print(f'{self} rolled a {roll} ({self.score})')

    def has_won(self):
        return self.score >= 100

    def __str__(self):
        return f'Player {self.num_players}'

    def __repr__(self):
        return f'Player {self.num_players}'