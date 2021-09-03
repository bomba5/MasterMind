#!/usr/bin/env python3

import random

from common import result_t
from codeMaker import CodeMaker

if __name__ == "__main__":

    myGuess = list (random.choice ("BRYVOG") for _ in range (4))
    loop = CodeMaker()

    print (loop._gameCode)
    print (myGuess)
    print (loop.checkGuess (myGuess))
