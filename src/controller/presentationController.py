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
        self.__timeTransition = 3
        self.__time = pygame.time.get_ticks()

    def action(self,event):
        if event.type == pygame.QUIT:
            sys.exit(0)
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.__shared["page"] = Page.HOME
            return Page.NEXT
        

    def transition(self):
        currentTime =  (pygame.time.get_ticks() - self.__time)//1000
        if int(currentTime) > self.__timeTransition:
            self.__time = pygame.time.get_ticks()
            self.__view.changeView()

    def update(self,sharedUpdate):
        self.__shared = sharedUpdate
        self.__view.refreshView(self.__shared)

    def run(self):
        while True:
            self.transition()
            self.__view.drawAll()
            for event in pygame.event.get():
                if self.action(event) == Page.NEXT:
                    return self.__shared
                self.__view.update(event)

            if self.__view.getTransitionNum() == 4 :
                self.__shared["page"] = Page.HOME
                return self.__shared