import pygame, sys, os
from pygame.locals import *
pygame.init()
sys.path.append(os.getcwd())
from model.enums.modeGame import ModeGame
from model.enums.page import Page
from controller.gameController import GameController
from controller.homeController import HomeComtroller
from controller.unavailableVController import UnavailableComtroller

class App:
    def __init__(self):
        self.loadFonts()
        self.__dimWindow = (720,400)
        self.__common = {"window":pygame.display.set_mode(self.__dimWindow),
                         "bg":pygame.image.load("src/ressources/images/app/background.jpg"),
                         "mode":ModeGame.HUMAN,
                         "page":Page.GAME,
                         "fonts":self.__fonts}
        self.__controllers = [HomeComtroller(self.__common),
                              GameController(self.__common),
                              UnavailableComtroller(self.__common)]
        
        self.__icon = pygame.image.load("src/ressources/images/app/icon.ico")
        pygame.display.set_icon(self.__icon)
        self.__currentPage = self.__common["page"].value
         
    def run(self):
        while True:
            self.__controllers[self.__currentPage].update(self.__common)
            self.__common = self.__controllers[self.__currentPage].run()
            self.__currentPage = self.__common["page"].value

    def loadFonts(self):
        self.__fonts = []
        self.__fonts.append("src/ressources/fonts/full_pack_2025/full Pack 2025.ttf")
        self.__fonts.append("src/ressources/fonts/freshman/Freshman.ttf")
        self.__fonts.append("src/ressources/fonts/karmatic_arcade/ka1.ttf")
        self.__fonts.append("src/ressources/fonts/super_mario_256/SuperMario256.ttf")

if __name__ == "__main__":
    App().run()
    pygame.quit()