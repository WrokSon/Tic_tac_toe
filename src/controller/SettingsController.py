import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from controller.controller import Controller
from model.enums.page import Page
from model.enums.modeGame import ModeGame
from view.SettingsView import SettingsView
pygame.init()

class SettingsController(Controller):
    def __init__(self,shared):
        self.__shared = shared
        self.__view = SettingsView(self.__shared)
        self.__musicOn = True
    
    def action(self,event):
        if event.type == pygame.QUIT:
            sys.exit(0)

        if self.__view.getValueBtnDefault():
            self.default()
            self.__view.refreshView(self.__shared)
            self.__view.setBtnTextMusicVolume("10%")
            self.__view.setValueBtnDefault()

        if self.__view.getValueBtnChangeBackgound():
            self.__view.setBackground(self.__view.getFileSelected())
            self.__view.setValueBtnChangeBackgound()

        if self.__view.getValueBtnHome() or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            self.__shared = self.__view.getShared()
            self.__shared["page"] = Page.HOME
            self.__view.setValueBtnHome()
            return Page.NEXT
            
        if self.__view.getValueBtnGame() and self.__shared["mode"] != ModeGame.NOMODE:
            self.__shared = self.__view.getShared()
            if self.__shared["mode"] == ModeGame.HUMAN: self.__shared["page"] = Page.GAME
            if self.__shared["mode"] == ModeGame.BOT: self.__shared["page"] = Page.GAMESOLO
            if self.__shared["mode"] == ModeGame.ONLINE: self.__shared["page"] = Page.GAMEONLINE
            self.__view.setValueBtnGame()
            return Page.NEXT

        self.actionBtnsMusic()
        self.actionBtnsProfile()

    def actionBtnsMusic(self):
        if self.__view.getValueBtnSetMusic():
            self.actionBtnMusicEdit("MusicGeneral")
            self.__view.setValueBtnSetMusic()
        
        if self.__view.getValueBtnSetMusicHuman():
            self.actionBtnMusicEdit("Music1V1")
            self.__view.setValueBtnSetMusicHuman()
        
        if self.__view.getValueBtnSetMusicSolo():
            self.actionBtnMusicEdit("MusicSolo")
            self.__view.setValueBtnSetMusicSolo()
        
        if self.__view.getValueBtnSetMusicOnLine():
            self.actionBtnMusicEdit("MusicOnLine")
            self.__view.setValueBtnSetMusicOnLine()
        
        if self.__view.getValueBtnSetMusicOn():
            self.__musicOn = not self.__musicOn
            self.__shared["MusicOn"] = self.__musicOn
            if self.__musicOn:
                self.playMusic("MusicGeneral")
                self.__view.setBtnTextMusicOn("ACTIVER")
            else:
                pygame.mixer.music.stop()
                self.__view.setBtnTextMusicOn("DESACTIVER")
            self.__view.setValueBtnSetMusicOn()
        
        if self.__view.getValueBtnSetMusicVolume():
            self.actionBtnMusicVolume()

    def actionBtnsProfile(self):

        if self.__view.getValueBtnSetProfileImage1():
            self.actionBtnsProfileImage("ImagePlayer1")
            self.__view.setValueBtnSetProfileImage1()
        
        if self.__view.getValueBtnSetProfileImage2():
            self.actionBtnsProfileImage("ImagePlayer2")
            self.__view.setValueBtnSetProfileImage2()
        
        if self.__view.getValueBtnSetProfileName1():
            self.actionBtnsProfileName("NamePlayer1")
            self.__view.setValueBtnSetProfileName1()
        
        if self.__view.getValueBtnSetProfileName2():
            self.actionBtnsProfileName("NamePlayer2")
            self.__view.setValueBtnSetProfileName2()
            self.__view.setValueBtnSetMusicVolume()
    
    def playMusic(self,value):
        if self.__shared["MusicOn"]:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(self.__shared[value])
            pygame.mixer.music.set_volume(self.__shared["MusicVolume"])
            pygame.mixer.music.play(-1,0.0)
            self.__shared["CurrentMusic"] = self.__shared[value]

    def actionBtnMusicEdit(self,value):
        music = self.__view.getFileSelected()
        if music != "":
            self.__shared[value] = music
            self.playMusic(value)

    def actionBtnMusicVolume(self):
        try:
            newVolume = self.__view.getValueInputBox()
            if newVolume != "":
                if int(newVolume) >= 0 and int(newVolume) <= 100:
                    volumeInt = int(newVolume)
                self.__shared["MusicVolume"] = float(volumeInt/100)
                pygame.mixer.music.set_volume(self.__shared["MusicVolume"])
                self.__view.setBtnTextMusicVolume(f"{volumeInt}%")
                self.__view.refreshView(self.__shared)
            self.__view.setValueInputBox() 
        except:
            pass

    def actionBtnsProfileName(self,value):
        newName = self.__view.getValueInputBox()
        if newName != "":
            self.__shared[value] = newName
            self.__view.refreshView(self.__shared)
        self.__view.setValueInputBox()
    
    def actionBtnsProfileImage(self,value):
        img = self.__view.getFileSelected()
        if img != "":
            self.__shared[value] = img
            self.__view.refreshView(self.__shared)
        
    def update(self,sharedUpdate):
        #pour mettre a jour le des infos partagés
        self.__shared = sharedUpdate
        self.__view.refreshView(self.__shared)

    def default(self):
        self.__shared["bg"] = "src/resources/images/app/background.jpg"
        self.__shared["NamePlayer1"] = "Joueur 1"
        self.__shared["NamePlayer2"] = "Joueur 2"
        self.__shared["ImagePlayer1"] = "src/resources/images/profile/profilePlayerDefault.png"
        self.__shared["ImagePlayer2"] = "src/resources/images/profile/profilePlayerDefault.png"
        self.__shared["Music1V1"] = "src/resources/musics/drum-percussion-beat-118810.mp3"
        self.__shared["MusicGeneral"] = "src/resources/musics/hitting-hard-cinematic-rock-trailer-142396.mp3"
        self.__shared["MusicSolo"] = "src/resources/musics/motivation-hip-hop-epic-sport-hip-hop-background-music-124924.mp3"
        self.__shared["MusicOnLine"] = "src/resources/musics/trap-beat-99191.mp3"
        self.__shared["MusicOn"] = True
        self.__shared["MusicVolume"] = 0.1
        self.__musicOn = True
        self.__view.setBtnTextMusicOn("ACTIVER")
        self.playMusic("MusicGeneral")

    def run(self):
        while True:
            self.__view.drawAll()
            for event in pygame.event.get():
                if self.action(event) == Page.NEXT:
                    return self.__shared
                self.__view.update(event)

