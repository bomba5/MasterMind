## MasterMind

[![YouTube demo](https://i.imgur.com/YfRuPOZ.png)](https://www.youtube.com/watch?v=5F2OB59lLmg "YouTube demo")
[*Click for YouTube demo*](https://www.youtube.com/watch?v=5F2OB59lLmg)

#### What is this MasterMind repo?
This is a sketchy implementation for both CodeMaker and CodeBreaker side.
The game is playble through Telegram.

The Telegram interface has been made with [*python-telegram-bot*](https://github.com/python-telegram-bot/python-telegram-bot) wrapper.

On the popular MasterMind game side, I've took inspiration from [*this online version of the game*](https://www.archimedes-lab.org/mastermind.html).

For the CodeBreaker code, I've been digging a lot of resources, mainly about MinMax algorithm, Donald Knuth and Peter F. Swaszek demonstrations.
In particular, [*this talk*](https://www.youtube.com/watch?v=UtX8W3fGh9k) from [*Adam Forsyth*](https://github.com/agfor) has been a source of inspiration.

A living example of this bot may be found here: [*@mastermind_solver_bot*](https://t.me/mastermind_solver_bot) according to my test server availability.

#### Telegram or console?
By uncommenting from line 15 to line 18 of masterMind.py, it is possible to just check the CodeBreaker side, without bringing up the whole Telegram interface.

#### What is required?
You will need:
- Python3
- Python-pip3

You can resolve python module dependencies by:
```sh
sudo pip3 install -r requirements.txt
```

*Config:*
- Edit ***conf/token.conf.dist*** using your token received from BotFather and save it to ***conf/token.conf***
