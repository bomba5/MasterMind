#!/usr/bin/env python3

from codeMaker import CodeMaker
from codeBreaker import CodeBreaker
from telegramWrapper import TelegramWrapper


def __main__ ():
    """
    """
    game = CodeMaker ()
    player = CodeBreaker ()

    # ---> Uncomment for solo codeBreaker
    #game.newGame ()
    #player.newGame (game)
    #player.play ()
    #exit (0)
    # <---

    bot = TelegramWrapper (game, player)
    bot.loop ()

if __name__ == "__main__":
    __main__ ()
