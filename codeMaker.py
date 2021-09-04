import random, collections

from common import Results

class CodeMaker:

    def __init__ (self):
        """
        """
        self.gameCode = list (random.choice (range (6)) for _ in range (4))
        print ("-- CodeMaker - generated code: {}".format (self.gameCode))


    def checkGuess (self, guess):
        """
            Returns Results type containing feedback of black and
            white pins
        """
        blackPins = 0
        whitePins = 0
        wrongGuessElements = []
        wrongAnswerElements = []

        print ("-- CodeMaker - checking against: {}".format (self.gameCode))

        for guessElement, answerElement in zip (guess, self.gameCode):
            if guessElement == answerElement:
                blackPins += 1
            else:
                wrongGuessElements.append (guessElement)
                wrongAnswerElements.append (answerElement)

        for wrongGuess in wrongGuessElements:
            if wrongGuess in wrongAnswerElements:
                wrongAnswerElements.remove (wrongGuess)
                whitePins += 1

        if (blackPins == 4):
            print ("-- CodeMaker - Masterminded!!!")

        return Results (blackPins, whitePins)
