import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from model.enums.page import Page
from view.SettingsView import SettingsView
pygame.init()

class SettingsController:
    def __init__(self,shared):
        self.__shared = shared
        self.__view = SettingsView(self.__shared)
    
    def action(self,event):
        if event.type == pygame.QUIT:
            sys.exit(0)

        if self.__view.getValueBtnDefault():
            self.default()
            self.__view.refreshView(self.__shared)
            self.__view.setValueBtnDefault()

        if self.__view.getValueBtnChangeBackgound():
            self.__view.setBackground(self.__view.getFileSelected())
            self.__view.setValueBtnChangeBackgound()

        if self.__view.getValueBtnHome():
            self.__shared = self.__view.getShared()
            self.__shared["page"] = Page.HOME
            self.__view.setValueBtnHome()
            return Page.NEXT
            
        if self.__view.getValueBtnGame():
            self.__shared = self.__view.getShared()
            self.__shared["page"] = Page.GAME
            self.__view.setValueBtnGame()
            return Page.NEXT

        self.actionBtnsMusic()
        self.actionBtnsProfile()

    def actionBtnsMusic(self):
        if self.__view.getValueBtnSetMusic():
            #a modifer de le son
            self.__view.setValueBtnSetMusic()
        
        if self.__view.getValueBtnSetMusicHuman():
            #a modifer de le son
            self.__view.setValueBtnSetMusicHuman()
        
        if self.__view.getValueBtnSetMusicSolo():
            #a modifer de le son
            self.__view.setValueBtnSetMusicSolo()
        
        if self.__view.getValueBtnSetMusicOnLine():
            #a modifer de le son
            self.__view.setValueBtnSetMusicOnLine()
        
        if self.__view.getValueBtnSetMusicOn():
            #a desactiver le son
            self.__view.setValueBtnSetMusicOn()

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
    
    def actionBtnsProfileName(self,value):
        newName = self.__view.getValueInputBox()
        if newName != "":
            self.__shared[value] = newName
            self.__view.refreshView(self.__shared)
        self.__view.setValueInputBox()
    
    def actionBtnsProfileImage(self,value):
        img = self.__view.getFileSelected()
        if img != "":
            self.__shared[value] = pygame.image.load(img)
            self.__view.refreshView(self.__shared)

    def update(self,sharedUpdate):
        #pour mettre a jour le des infos partagés
        self.__shared = sharedUpdate
        self.__view.refreshView(self.__shared)

    def default(self):
        self.__shared["bg"] = pygame.image.load("src/ressources/images/app/background.jpg")
        self.__shared["NamePlayer1"] = "Joueur 1"
        self.__shared["NamePlayer2"] = "Joueur 2"
        self.__shared["ImagePlayer1"] = pygame.image.load("src/ressources/images/profile/profilePlayerO.jpg")
        self.__shared["ImagePlayer2"] = pygame.image.load("src/ressources/images/profile/profilePlayerX.jpg")

    def run(self):
        while True:
            self.__view.drawAll()
            for event in pygame.event.get():
                if self.action(event) == Page.NEXT:
                    return self.__shared
                self.__view.update(event)