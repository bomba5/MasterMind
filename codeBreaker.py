import random, itertools

from common import Results


class CodeBreaker:

    def __init__ (self, ctx):
        """
        """
        # Get the current game context
        self.game = ctx


    def findCorrectMatch (self, actual, guess):
        """
            Finds the sum of matched pins
        """
        return sum ([1 for (a, b) in zip (actual, guess) if a == b])


    def findCloseMatch (self, current, guess):
        """
            Finds the sum of mismatched but present pins
        """
        close = 0

        # Remove matched pins
        l_current = [a for (a, b) in zip (current, guess) if a != b]
        l_guess = [b for (a, b) in zip (current, guess) if a != b]

        for possible in l_guess:
            if possible in l_current:
                del l_current[l_current.index(possible)]
                close += 1

        return close


    def match (self, guess, possibleAnswer, result):
        """
            Returns true if passed result matches possible answer results
        """
        return result == Results (
                self.findCorrectMatch (possibleAnswer, guess),
                self.findCloseMatch (possibleAnswer, guess)
                )


    def filterPossible (self, guess, possibleAnswers, result):
        """
            Iterates throught possible pool and removes impossible answers
        """
        for answer in possibleAnswers:
            if self.match (guess, answer, result) and (answer != guess):
                yield answer


    def guessAnswer (self, possibleAnswers, result):
        """
            Chooses the best guess within the possible answers
        """
        minLength = float ('infinity')
        nextGuess = None

        for answer in possibleAnswers:
            currentLength = len (
                    list (self.filterPossible (answer, possibleAnswers, result))
                    )

            if minLength > currentLength:
                minLength = currentLength
                nextGuess = answer

        return nextGuess


    def play (self):
        """
        """
        guessNumber = 0

        # Calculate Cartesian product for 4 numbers in range 0-6
        # representing all the possible combinations
        possibleAnswers = list (
                itertools.product (*[range (6) for _ in range (4)])
                )

        # This will be my opening guess
        myGuess = [0, 0, 1, 1]

        while (guessNumber < 10):
            print ("#{} CodeBreaker - guessing: {}".format (
                (guessNumber + 1), myGuess))

            # Collect the current guess results
            guessResult = self.game.checkGuess (myGuess)

            # Element 0 contains the count of black pins
            # if 4, we won
            if (guessResult[0] == 4):
                break

            # Filters the possible answers removing the current guess
            # and the other imbossible ones
            possibleAnswers = list (
                    self.filterPossible (myGuess, possibleAnswers, guessResult)
                    )

            # Compute the new guess
            myGuess = self.guessAnswer (possibleAnswers, guessResult)

            guessNumber += 1
