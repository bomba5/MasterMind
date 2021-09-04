import collections

Results = collections.namedtuple("Results", ["blackPins", "whitePins"])

CONFIG_FILE = "./conf/token.conf"


def findCorrectMatch (current, guess):
    """
        Returns the sum of matching pins
    """

    # Just the total of matching pins
    return sum ([1 for (a, b) in zip (current, guess) if a == b])


def findCloseMatch (current, guess):
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

    # Return number of close matches
    return close


def validateUserGuess (userGuess):
    """
        Validate user input:
        Input should be 4 digits in range 0-5.
        Return None if rules are broken.
    """
    resGuess = []

    for digit in userGuess:
        if digit.isdigit():
            if int (digit) in range (6):
                resGuess.append (int (digit))
            else:
                resGuess = None
                break
        else:
            resGuess = None
            break

    if resGuess and len (resGuess) != 4:
        resGuess = None

    return resGuess
