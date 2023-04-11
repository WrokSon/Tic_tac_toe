import pygame, sys, os
sys.path.append(os.getcwd())
from model.enums.modeGame import ModeGame
from model.enums.page import Page
from view.homeView import HomeWiew

class HomeComtroller:
    def __init__(self,shared):
        self.__shared = shared
        self.__mode = self.__shared["mode"]
        self.__view = HomeWiew(self.__shared)
    
    def action(self,event):
        if event.type == pygame.QUIT:
            sys.exit(0)
        
        if self.__view.getValueBtnBotGo():
            self.__shared["page"] = Page.UNAVAILABLE
            self.__shared["mode"] = ModeGame.BOT
            self.__view.setValueBtnBotGo()
            return Page.NEXT
        
        if self.__view.getValueBtnHumanGo():
            self.__shared["page"] = Page.GAME
            self.__shared["mode"] = ModeGame.HUMAN
            self.__view.setValueBtnHumanGo()
            return Page.NEXT
        
        if self.__view.getValueBtnOnLine():
            self.__shared["page"] = Page.UNAVAILABLE
            self.__shared["mode"] = ModeGame.ONLINE
            self.__view.setValueBtnOnLine()
            return Page.NEXT
        
        if self.__view.getValueBtnSettings():
            self.__shared["page"] = Page.SETTINGS
            self.__view.setValueBtnSettings()
            return Page.NEXT

    def update(self,sharedUpdate):
        #pour mettre a jour le des infos partagés
        self.__shared = sharedUpdate
        self.__view.refreshView(self.__shared)

    def run(self):
        while True:
            self.__view.drawAll()
            for event in pygame.event.get():
                if self.action(event) == Page.NEXT:
                    return self.__shared
                self.__view.update(event)