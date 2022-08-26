"""
    Simulate a simple board game.
    There are 2 players.
    Each player takes turn rolling a die and moving that number of spaces.
    The first person to space 100 wins.
"""

from random import randint


def play_game(num_players=2):
    # create a scores list with 0 initial values for number of players
    # lets take 3 players then scores list will be like scores[0, 0, 0]
    scores = [0 for _ in range(num_players)]

    while True:
        for i, score in enumerate(scores):
            player_num = i + 1  # initial i value will be 0 so increment with 1
            roll = randint(1, 6)
            score += roll

            # increase the score
            scores[i] = score

            print(f'player {player_num} rolled a {roll} ({score})')

            if score >= 100:
                print(f'Player {player_num} wins!')
                return


if __name__ == '__main__':
    play_game(num_players=3)
