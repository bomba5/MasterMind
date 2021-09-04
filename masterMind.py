#!/usr/bin/env python3

from codeMaker import CodeMaker
from codeBreaker import CodeBreaker

if __name__ == "__main__":
    # Init the game
    game = CodeMaker ()

    # Init the player, while passing the current game
    player = CodeBreaker (game)

    # Let him play
    player.play ()

