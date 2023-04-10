import pygame, sys, os
from pygame.locals import *
pygame.init()
sys.path.append(os.getcwd())
from controller.gameController import GameController

class App:
    def __init__(self):
        self.__dimWindow = (720,400)
        self.__window = pygame.display.set_mode(self.__dimWindow)
        print(os.getcwd())
        self.__icon = pygame.image.load("src/ressources/images/app/icon.ico")
        pygame.display.set_icon(self.__icon)
        self.__controllers = [GameController(self.__window)]
        self.__currentController = 0
    
    def run(self):
        self.__controllers[self.__currentController].run()

if __name__ == "__main__":
    App().run()
    pygame.quit()