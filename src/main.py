import pygame, sys, os, socket
from pygame.locals import *
pygame.init()
pygame.mixer.init()
sys.path.append(os.getcwd())
from model.enums.modeGame import ModeGame
from model.enums.page import Page
from controller.gameController import GameController
from controller.homeController import HomeComtroller
from controller.SettingsController import SettingsController
from controller.launcherGameController import LauncherGameController
from controller.unavailableController import UnavailableController
from controller.presentationController import PresentationController

class App:
    def __init__(self):
        self.__dimWindow = (720,400)
        self.__myIpAddr = socket.gethostbyname(socket.gethostname())  
        self.loadAll()
        self.__icon = pygame.image.load("src/resources/images//icons/app/icon.ico")
        pygame.display.set_icon(self.__icon)
        self.__currentPage = self.__shared["page"].value
         
    def run(self):
        while True:
            self.__controllers[self.__currentPage].update(self.__shared)
            self.__shared = self.__controllers[self.__currentPage].run()
            self.__currentPage = self.__shared["page"].value

    def loadFonts(self):
        self.__fonts = []
        self.__fonts.append("src/resources/fonts/full_pack_2025/full Pack 2025.ttf")
        self.__fonts.append("src/resources/fonts/freshman/Freshman.ttf")
        self.__fonts.append("src/resources/fonts/karmatic_arcade/ka1.ttf")
        self.__fonts.append("src/resources/fonts/super_mario_256/SuperMario256.ttf")

    def loadAll(self):
        self.loadFonts()
        self.loadIcons()
        self.loadCommon()
        self.loadControllerPages()
    
    def loadCommon(self):
        self.__shared = {}
        self.__shared["window"] = pygame.display.set_mode(self.__dimWindow)
        self.__shared["bg"] = "src/resources/images//icons/app/background.jpg"
        self.__shared["mode"] = ModeGame.NOMODE
        self.__shared["page"] = Page.PRESENTATION
        self.__shared["fonts"] = self.__fonts
        self.__shared["icons"] = self.__icons
        self.__shared["NamePlayer1"] = "Joueur 1"
        self.__shared["NamePlayer2"] = "Joueur 2"
        self.__shared["ImagePlayer1"] = "src/resources/images/profile/profilePlayerDefault.png"
        self.__shared["ImagePlayer2"] = "src/resources/images/profile/profilePlayerDefault.png"
        self.__shared["CurrentMusic"] = ""
        self.__shared["Music1V1"] = "src/resources/musics/drum-percussion-beat-118810.mp3"
        self.__shared["MusicGeneral"] = "src/resources/musics/hitting-hard-cinematic-rock-trailer-142396.mp3"
        self.__shared["MusicSolo"] = "src/resources/musics/motivation-hip-hop-epic-sport-hip-hop-background-music-124924.mp3"
        self.__shared["MusicOnLine"] = "src/resources/musics/trap-beat-99191.mp3"
        self.__shared["MusicOn"] = True
        self.__shared["MusicVolume"] = 0.1
        self.__shared["difficulty"] = "Facile"
        self.__shared["difficultyList"] = ["Facile","Difficle"]
        self.__shared["server"] = False
        self.__shared["isConnected"] = False
        self.__shared["IpAddrServer"] = self.__myIpAddr
        self.__shared["IpAddrClient"] = self.__myIpAddr
        self.__shared["port"] = 7639
        self.__shared["msgPlayers"] = ["Bienvenu(e)","Bienvenu(e)"]
        self.__shared["typConnection"] = ["INVITE","HOTE"]

    def loadIcons(self):
        self.__icons = []
        self.__icons.append("src/resources/images/icons/settings.png")
        self.__icons.append("src/resources/images/icons/download.png")
        self.__icons.append("src/resources/images/icons/restart.png")
        self.__icons.append("src/resources/images/icons/home.png")
        self.__icons.append("src/resources/images/icons/back.png")
        self.__icons.append("src/resources/images/icons/default.png")
        self.__icons.append("src/resources/images/icons/edit/text.png")
        self.__icons.append("src/resources/images/icons/edit/image.png")
        self.__icons.append("src/resources/images/icons/edit/music.png")



    def loadControllerPages(self):
        self.__controllers = []
        self.__controllers.append(PresentationController(self.__shared))
        self.__controllers.append(HomeComtroller(self.__shared))
        self.__controllers.append(LauncherGameController(self.__shared))
        self.__controllers.append(GameController(self.__shared))
        self.__controllers.append(UnavailableController(self.__shared))
        self.__controllers.append(SettingsController(self.__shared))

if __name__ == "__main__":
    App().run()
    pygame.quit()