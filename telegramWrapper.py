from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import Filters, CallbackQueryHandler
from telegram.ext.dispatcher import run_async

from common import CONFIG_FILE
from codeMaker import CodeMaker
from codeBreaker import CodeBreaker


class TelegramWrapper:

    def __init__ (self):
        """
        """
        try:
            self.token = open (CONFIG_FILE, "r").read ().replace ("\n", "")
        except Exception as e:
            print ("-- TelegramWrapper - could not find '{}'".format (CONFIG_FILE))
            exit (1)


    def commandStart (self, bot, update):
        """
        """
        # Init new MasterMind game
        game = CodeMaker ()
        player = CodeBreaker (game)
        player.play ()


    def commandHelp (self, bot, update):
        """
        """


    def commandUnknown (self, bot, update):
        """
        """


    def commandError (self, bot, update, error):
        """
        """


    def loop (self):
        """
        """
        # Create event handler with botFather's token
        self.updater = Updater (self.token)

        # Get the dispatcher and register command/error handlers
        self.dp = self.updater.dispatcher
        self.dp.add_handler (CommandHandler ("start", self.commandStart))
        self.dp.add_handler (CommandHandler ("help", self.commandHelp))
        self.dp.add_handler (MessageHandler (Filters.command, self.commandUnknown))
        self.dp.add_error_handler (self.commandError)

        # Start the bot
        self.updater.start_polling ()
        print ("-- TelegramWrapper - bot started")

        #self.updater.idle ()
