import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from model.enums.page import Page
from view.unavailableView import UnavailableView
pygame.init()

class UnavailableController:
    def __init__(self,shared):
        self.__shared = shared
        self.__view = UnavailableView(self.__shared)
    
    def action(self,event):
        if event.type == pygame.QUIT:
            sys.exit(0)
        if self.__view.getValueBtnHome():
            self.__shared["page"] = Page.HOME
            self.__view.setValueBtnHome()
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