from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import Filters, CallbackQueryHandler
from telegram.ext.dispatcher import run_async

from common import CONFIG_FILE, validateUserGuess


class TelegramWrapper:

    def __init__ (self, MastermindGame, MastermindBreaker):
        """
            Initialize member values and load Telegram token
        """
        self.game = MastermindGame
        self.breaker = MastermindBreaker
        self.gameStarted = False
        self.gameAttempt = 0
        self.result = None

        try:
            self.token = open (CONFIG_FILE, "r").read ().replace ("\n", "")
        except Exception as e:
            print ("-- TelegramWrapper - could not find '{}'".format (CONFIG_FILE))
            exit (1)


    def commandStart (self, update, context):
        """
            Type credits and summarize commands
        """
        update.message.reply_text("MasterMind - CodeMaker/CodeBreaker")
        update.message.reply_text("Coded by Jhonata Poma for TechPeople")
        update.message.reply_text("Type /play to play a MasterMind game")
        update.message.reply_text(
                "Type /auto to watch CodeBreaker win a MasterMind game"
                )
        update.message.reply_text(
                "Goal of the /play game is to find the right combination of " \
                "four numbers from zero to five. If a number is correct and " \
                "in the correct position, you will get one 'black'; If a " \
                "number is present but in a different postion, you will get " \
                "a 'white'."
                )
        update.message.reply_text(
                "When in mode /auto, codeMaker will generate and show a " \
                "combination of four numbers from zero to fiven, and then " \
                "the codeBreaker algorithm will try to find it in the " \
                "shortest number of attempts."
                )


    def commandPlay (self, update, context):
        """
            Play a game of MasterMind as CodeBreaker
        """
        self.gameStarted = True
        self.gameAttempt = 0

        # Init new MasterMind game
        self.game.newGame ()

        update.message.reply_text("Started new MasterMind game")
        update.message.reply_text("Input 4 numbers (0-5)")


    def commandAuto (self, update, context):
        """
            Watch a game of MasterMind played by bot CodeBreaker
        """
        self.gameStarted = True
        self.gameAttempt = 0

        blackPins = 0

        # Init new MasterMind game
        self.game.newGame ()

        # Init new MasterMind codeBreaker bot
        self.breaker.newGame (self.game)

        update.message.reply_text("Started new MasterMind game")
        update.message.reply_text("CodeBreaker will solve it for you :)")
        update.message.reply_text("Code to find is: {}".format (
            self.game.gameCode))

        while (blackPins != 4):
            nextMove = self.breaker.nextMove (self.result)
            update.message.reply_text(
                    "CodeBreaker is trying: {}".format (nextMove))

            self.gameAttempt += 1
            self.result = self.game.checkGuess (nextMove)

            update.message.reply_text(
                    "Attempt #{} - Blacks: {} - Whites: {}".format (
                        self.gameAttempt, self.result[0], self.result[1])
                    )

            blackPins = self.result[0]

        update.message.reply_text(
                "MASTERMINDED! Code found in {} attempts".format (
                    self.gameAttempt))

        self.gameStarted = False
        self.gameAttempt = 0


    def commandText (self, update, context):
        """
            If game session started, get the user input as the next move
        """
        if (self.gameStarted):
            userGuess = validateUserGuess (update.message.text)
            if (userGuess):
                self.gameAttempt += 1
                self.result = self.game.checkGuess (userGuess)
                print ("-- TelegramWrapper - user guess: {}". format (userGuess))
                update.message.reply_text(
                        "Attempt #{} - Blacks: {} - Whites: {}".format (
                            self.gameAttempt, self.result[0], self.result[1])
                    )

                if (self.result[0] == 4):
                    self.gameStarted = False
                    self.gameAttempt = 0
                    update.message.reply_text("MASTERMINDED!")
            else:
                update.message.reply_text("Guess '{}' is not valid".format(
                    update.message.text))
                update.message.reply_text("Input 4 numbers (0-5)")
        else:
            update.message.reply_text("Game not started yet!")
            update.message.reply_text("Type /start to... start.")


    def loop (self):
        """
            Bot's handlers adding and main loop
        """
        # Create event handler with botFather's token
        self.updater = Updater (self.token)

        # Get the dispatcher and register command handlers
        self.dp = self.updater.dispatcher
        self.dp.add_handler (CommandHandler ("start", self.commandStart))
        self.dp.add_handler (CommandHandler ("play", self.commandPlay))
        self.dp.add_handler (CommandHandler ("auto", self.commandAuto))
        self.dp.add_handler (MessageHandler (Filters.text, self.commandText))

        # Start the bot
        self.updater.start_polling ()
        print ("-- TelegramWrapper - bot started")

        self.updater.idle ()
