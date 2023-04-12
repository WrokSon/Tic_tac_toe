import sys, os
sys.path.append(os.getcwd())
from enum import Enum

class Page(Enum):
    NEXT = -1
    PRESENTATION = 0
    HOME = 1
    LAUNCHERGAME = 2
    GAME = 3
    GAMESOLO = 4
    GAMEONLINE = 4
    SETTINGS = 5
    UNAVAILABLE = 4