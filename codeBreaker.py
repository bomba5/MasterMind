import random, itertools

from common import Results, findCorrectMatch, findCloseMatch


class CodeBreaker:

    def __init__ (self):
        """
            Empty contructor
        """


    def newGame (self, ctx):
        """
            Initialize new game
        """
        # Get the current game context
        self.game = ctx

        self.guessNumber = 0

        # Calculate Cartesian product for 4 numbers in range 0-6
        # representing all the possible combinations
        self.possibleAnswers = list (
                itertools.product (*[range (6) for _ in range (4)])
                )

        # This will be my opening guess
        self.myGuess = [0, 0, 1, 1]


    def guessResult (self, guess, possibleAnswer, result):
        """
            Returns true if passed result matches possible answer results
        """

        # If computed results matches current result, return true
        return result == Results (
                findCorrectMatch (possibleAnswer, guess),
                findCloseMatch (possibleAnswer, guess)
                )


    def filterPossible (self, guess, possibleAnswers, result):
        """
            Iterates throught possible pool and yeld improving answers
        """
        for answer in possibleAnswers:
            if self.guessResult (guess, answer, result) and (answer != guess):
                yield answer
            # else: Discarding answer


    def guessAnswer (self, possibleAnswers, result):
        """
            Chooses the best guess within the possible answers
        """
        minLength = float ('infinity')
        nextGuess = None

        # For each answer in possible answers, calculate the length
        # of the remaining possible answers list.
        # Choose the answer which generates the shortest remaining list.
        for answer in possibleAnswers:
            currentLength = len (
                    list (self.filterPossible (answer, possibleAnswers, result))
                    )

            if minLength > currentLength:
                minLength = currentLength
                nextGuess = answer

        return nextGuess


    def nextMove (self, guessResult):
        """
            Define next move for the Telegram game.
            Part of this code is also present in the following
            original Play function.
        """
        if (self.guessNumber != 0):
            # Filters the possible answers removing the current guess
            # and the other imbossible ones
            self.possibleAnswers = list (
                    self.filterPossible (
                        self.myGuess, self.possibleAnswers, guessResult)
                    )

            # Compute the new guess
            self.myGuess = self.guessAnswer (self.possibleAnswers, guessResult)

        self.guessNumber += 1

        return self.myGuess


    def play (self):
        """
            Play a solo game:
            CodeBreaker will find the solution.
            Not suitable for Telegram Wrapping.
        """
        self.guessNumber = 0

        # Calculate Cartesian product for 4 numbers in range 0-6
        # representing all the possible combinations
        self.possibleAnswers = list (
                itertools.product (*[range (6) for _ in range (4)])
                )

        # This will be my opening guess
        self.myGuess = [0, 0, 1, 1]

        while (self.guessNumber < 10):
            print ("#{} CodeBreaker - guessing: {}".format (
                (self.guessNumber + 1), self.myGuess))

            # Collect the current guess results
            guessResult = self.game.checkGuess (self.myGuess)

            # Element 0 contains the count of black pins
            # if 4, we won
            if (guessResult[0] == 4):
                break

            # Filters the possible answers removing the current guess
            # and the other imbossible ones
            self.possibleAnswers = list (
                    self.filterPossible (
                        self.myGuess, self.possibleAnswers, guessResult)
                    )

            # Compute the new guess
            self.myGuess = self.guessAnswer (self.possibleAnswers, guessResult)

            self.guessNumber += 1
