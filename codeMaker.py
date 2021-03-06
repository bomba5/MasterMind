import random, collections

from common import Results, findCorrectMatch, findCloseMatch


class CodeMaker:

    def __init__ (self):
        """
            Empty constructor
        """


    def checkGuess (self, guess):
        """
            Returns Results type containing feedback of black and
            white pins
        """
        print ("-- CodeMaker - checking solution: {}".format (guess))
        print ("-- CodeMaker - against gameCode:  {}".format (self.gameCode))

        blackPins = findCorrectMatch (self.gameCode, guess)
        whitePins = findCloseMatch (self.gameCode, guess)

        if (blackPins == 4):
            print ("-- CodeMaker - Masterminded!!!")

        return Results (blackPins, whitePins)


    def newGame (self):
        """
            Initialize game code
        """
        self.gameCode = list (random.choice (range (6)) for _ in range (4))
        print ("-- CodeMaker - generated code: {}".format (self.gameCode))
