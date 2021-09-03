#!/usr/bin/env python3

from common import result_t
import random

class CodeMaker:

    def __init__ (self):
        """
        """
        self._gameCode = list (random.choice ("BRYVOG") for _ in range (4))


    def checkGuess (self, guess):
        """
        """
        result = result_t
        wrongGuessElements = []
        wrongAnswerElements = []

        for guessElement, answerElement in zip (guess, self._gameCode):
            if guessElement == answerElement:
                result["BLACK"] += 1
            else:
                wrongGuessElements.append (guessElement)
                wrongAnswerElements.append (answerElement)

        for wrongGuess in wrongGuessElements:
            if wrongGuess in wrongAnswerElements:
                wrongAnswerElements.remove (wrongGuess)
                result["WHITE"] += 1

        return result
