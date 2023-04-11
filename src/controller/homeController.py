import pygame, sys, os
sys.path.append(os.getcwd())
from model.enums.modeGame import ModeGame
from model.enums.page import Page
from view.homeView import HomeWiew

class HomeComtroller:
    def __init__(self,common):
        self.__common = common
        self.__mode = self.__common["mode"]
        self.__view = HomeWiew(self.__common)
    
    def action(self,event):
        if event.type == pygame.QUIT:
            sys.exit(0)
        
        if self.__view.getValueBtnBotGo():
            self.__common["page"] = Page.UNAVAILABLE
            self.__common["mode"] = ModeGame.BOT
            self.__view.setValueBtnBotGo()
            return Page.NEXT
        
        if self.__view.getValueBtnHumanGo():
            self.__common["page"] = Page.GAME
            self.__common["mode"] = ModeGame.HUMAN
            self.__view.setValueBtnHumanGo()
            return Page.NEXT
        
        if self.__view.getValueBtnOnLine():
            self.__common["page"] = Page.UNAVAILABLE
            self.__common["mode"] = ModeGame.ONLINE
            self.__view.setValueBtnOnLine()
            return Page.NEXT
        
        if self.__view.getValueBtnSettings():
            self.__common["page"] = Page.UNAVAILABLE
            self.__view.setValueBtnSettings()
            return Page.NEXT

    def update(self,update):
        #pour mettre a jour le common
        self.__common = update

    def run(self):
        while True:
            self.__view.drawAll()
            for event in pygame.event.get():
                if self.action(event) == Page.NEXT:
                    return self.__common
                self.__view.update(event)