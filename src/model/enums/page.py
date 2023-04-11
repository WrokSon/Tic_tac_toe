import sys, os
sys.path.append(os.getcwd())
from enum import Enum

class Page(Enum):
    NEXT = -1
    HOME = 0
    GAME = 1
    UNAVAILABLE = 2