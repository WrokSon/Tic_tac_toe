import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from model.enums.modeGame import ModeGame
from model.enums.page import Page
from view.unavailableView import UnavailableView
pygame.init()

class UnavailableComtroller:
    def __init__(self,common):
        self.__common = common
        self.__mode = self.__common["mode"]
        self.__view = UnavailableView(self.__common)
    
    def action(self,event):
        if event.type == pygame.QUIT:
            sys.exit(0)
        if self.__view.getValueBtnHome():
            self.__common["page"] = Page.HOME
            self.__view.setValueBtnHome()
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