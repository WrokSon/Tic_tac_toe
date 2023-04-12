import sys, os
sys.path.append(os.getcwd())
from enum import Enum

class ModeGame(Enum):
    NOMODE = 0
    HUMAN = 1
    BOT = 2
    ONLINE = 3