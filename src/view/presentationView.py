import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from view.view import View
from resources.tools.toolsDisplayable import Text

class PresentationView(View):
    def __init__(self,shared):
        self.__shared = shared
        self.__window = shared["window"]
        self.__windowTitle = "Tic Tac Toe | Presentation"

    def createAll(self):
        pass

    def drawAll(self):
        pygame.display.set_caption(self.__windowTitle)
        pygame.draw.rect(self.__window,"black",[(0,0),pygame.display.get_surface().get_size()])
        pygame.display.update()

    def update(self,event):
        pass

    def createBg(self):
        pass

    def refreshView(self,newShared):
        self.__shared = newShared
        self.createBg()