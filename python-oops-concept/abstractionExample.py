"""
    Simulate a simple board game.
    There are 2 players.
    Each player takes turn rolling a die and moving that number of spaces.
    The first person to space 100 wins.
"""

from Player import Player

def play_game(num_players=2):
    # create Player object in players array
    players = [Player(i + 1) for i in range(num_players)]

    print('----------Started Game with players----------------')
    print(players)
    print('----------proceed with rolling die-------------')

    while True:
        for player in players:
            player.make_move()
            if player.has_won():
                print(f'Player {player} wins!')
                return


if __name__ == '__main__':
    play_game(num_players=5)
