import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from controller.controller import Controller
from model.enums.page import Page
from model.enums.modeGame import ModeGame
from view.launcherGameHumanView import LauncherGameHumanView
from view.launcherGameOnLineView import LauncherGameOnLineView
from view.launcherGameSoloView import LauncherGameSoloView

pygame.init()

class LauncherGameController(Controller):
    def __init__(self,shared):
        self.__shared = shared
        self.__viewHumain = LauncherGameHumanView(self.__shared)
        self.__viewSolo = LauncherGameSoloView(self.__shared)
        self.__viewOnLine = LauncherGameOnLineView(self.__shared)

        if self.__shared["mode"] == ModeGame.HUMAN: self.__view = self.__viewHumain
        if self.__shared["mode"] == ModeGame.BOT: self.__view = self.__viewSolo
        if self.__shared["mode"] == ModeGame.ONLINE: self.__view = self.__viewOnLine
    
    def action(self,event):
        if event.type == pygame.QUIT:
            sys.exit(0)

        if self.__view.getValueBtnHome() or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            self.__shared["page"] = Page.HOME
            self.__view.setValueBtnHome()
            return Page.NEXT
        
        return self.actionHman()

    def actionHman(self):
        if self.__view.getValueBtnStart():
            if self.__shared["mode"] == ModeGame.HUMAN: self.__shared["page"] = Page.GAME
            if self.__shared["mode"] == ModeGame.BOT: self.__shared["page"] = Page.GAMESOLO
            if self.__shared["mode"] == ModeGame.ONLINE: self.__shared["page"] = Page.GAMEONLINE
            namePlayer1 = self.__view.getValueTIBPlayer1()
            namePlayer2 = self.__view.getValueTIBPlayer2()
            if namePlayer1 != "" : self.__shared["NamePlayer1"] = namePlayer1
            if namePlayer2 != "" : self.__shared["NamePlayer2"] = namePlayer2
            self.__view.setValueBtnStart()
            self.__view.setValueTIBPlayer1()
            self.__view.setValueTIBPlayer2()
            return Page.NEXT

        
    def update(self,sharedUpdate):
        #pour mettre a jour le des infos partagés
        self.__shared = sharedUpdate
        if self.__shared["mode"] == ModeGame.HUMAN: self.__view = self.__viewHumain
        if self.__shared["mode"] == ModeGame.BOT: self.__view = self.__viewSolo
        if self.__shared["mode"] == ModeGame.ONLINE: self.__view = self.__viewOnLine
        self.__view.refreshView(self.__shared)

    def run(self):
        while True:
            self.__view.drawAll()
            for event in pygame.event.get():
                if self.action(event) == Page.NEXT:
                    return self.__shared
                self.__view.update(event)
                