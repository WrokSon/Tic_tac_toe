import pygame, sys, os
from pygame.locals import *
pygame.init()
sys.path.append(os.getcwd())
from model.enums.modeGame import ModeGame
from model.enums.page import Page
from controller.gameController import GameController
from controller.homeController import HomeComtroller
from controller.SettingsController import SettingsController
from controller.unavailableController import UnavailableController

class App:
    def __init__(self):
        self.__dimWindow = (720,400)  
        self.loadAll()
        self.__icon = pygame.image.load("src/ressources/images/app/icon.ico")
        pygame.display.set_icon(self.__icon)
        self.__currentPage = self.__shared["page"].value
         
    def run(self):
        while True:
            self.__controllers[self.__currentPage].update(self.__shared)
            self.__shared = self.__controllers[self.__currentPage].run()
            self.__currentPage = self.__shared["page"].value

    def loadFonts(self):
        self.__fonts = []
        self.__fonts.append("src/ressources/fonts/full_pack_2025/full Pack 2025.ttf")
        self.__fonts.append("src/ressources/fonts/freshman/Freshman.ttf")
        self.__fonts.append("src/ressources/fonts/karmatic_arcade/ka1.ttf")
        self.__fonts.append("src/ressources/fonts/super_mario_256/SuperMario256.ttf")

    def loadAll(self):
        self.loadFonts()
        self.loadCommon()
        self.loadControllerPages()
    
    def loadCommon(self):
        self.__shared = {}
        self.__shared["window"] = pygame.display.set_mode(self.__dimWindow)
        self.__shared["bg"] = pygame.image.load("src/ressources/images/app/background.jpg")
        self.__shared["mode"] = ModeGame.HUMAN
        self.__shared["page"] = Page.HOME
        self.__shared["fonts"] = self.__fonts
        self.__shared["NamePlayer1"] = "Joueur 1"
        self.__shared["NamePlayer2"] = "Joueur 2"
        self.__shared["ImagePlayer1"] = pygame.image.load("src/ressources/images/profile/profilePlayerO.jpg")
        self.__shared["ImagePlayer2"] = pygame.image.load("src/ressources/images/profile/profilePlayerX.jpg")


    def loadControllerPages(self):
        self.__controllers = []
        self.__controllers.append(HomeComtroller(self.__shared))
        self.__controllers.append(GameController(self.__shared))
        self.__controllers.append(SettingsController(self.__shared))
        self.__controllers.append(UnavailableController(self.__shared))

if __name__ == "__main__":
    App().run()
    pygame.quit()