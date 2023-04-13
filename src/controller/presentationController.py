import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from controller.controller import Controller
from model.enums.page import Page
from view.presentationView import PresentationView
pygame.init()

class PresentationController(Controller):
    def __init__(self,shared):
        self.__shared = self.__shared = shared
        self.__view = PresentationView(shared)

    def action(self,event):
        if event.type == pygame.QUIT:
            sys.exit(0)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.__shared["page"] = Page.HOME
                return Page.NEXT

    def update(self,sharedUpdate):
        self.__shared = sharedUpdate
        self.__view.refreshView(self.__shared)

    def run(self):
        while True:
            self.__view.drawAll()
            for event in pygame.event.get():
                if self.action(event) == Page.NEXT:
                    return self.__shared
                self.__view.update(event)