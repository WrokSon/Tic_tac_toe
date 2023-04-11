import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from ressources.display.tools import Text, Button

pygame.init()

class HomeWiew:
    def __init__(self,shared):
        self.__shared = shared
        self.__windowTitle = "Tic Tac Toe | Page d'acceuille"
        self.__window = self.__shared["window"]
        self.__fonts = self.__shared["fonts"]
        self.createAll()
    
    def getValueBtnHumanGo(self):
        return self.__btnHumanGo.isActive()

    def getValueBtnBotGo(self):
        return self.__btnBotGo.isActive()

    def getValueBtnOnLine(self):
        return self.__btnOnLineGo.isActive()

    def getValueBtnSettings(self):
        return self.__btnSettings.isActive()
    
    def setValueBtnHumanGo(self):
        self.__btnHumanGo.notActive()

    def setValueBtnBotGo(self):
        self.__btnBotGo.notActive()

    def setValueBtnOnLine(self):
        self.__btnOnLineGo.notActive()

    def setValueBtnSettings(self):
        self.__btnSettings.notActive()

    def createAll(self):
        self.createBg()
        self.createButtons()
        self.creatTexts()
        pygame.display.update()
    
    def drawAll(self):
        self.__window.blit(self.__imgBg,(0,0))
        pygame.display.set_caption(self.__windowTitle)
        self.drawButtons()
        self.drawTexts()
        pygame.display.update()

    def doEvent(self,event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if self.__colorText == "yellow":
                self.__colorText = "black"
            else:
                self.__colorText = "yellow"

    def update(self,event):
        self.updateButtons(event)
        self.doEvent(event)

    def createBg(self):
        bgImg = self.__shared["bg"]
        self.__imgBg = pygame.transform.scale(bgImg, pygame.display.get_surface().get_size())

    def createButtons(self):
        self.createButtonsGo()
        self.__btnSettings = Button(self.__window,"*_*",position=(660,10),dimension=(50,50))

    def createButtonsGo(self):
        posBtn = [[i*150 for i in range(1,4)],300]
        self.__btnHumanGo = Button(self.__window,"1V1",position=(posBtn[0][0],posBtn[1]))
        self.__btnBotGo = Button(self.__window,"SOLO",position=(posBtn[0][1],posBtn[1]))
        self.__btnOnLineGo = Button(self.__window,"EN LIGNE",position=(posBtn[0][2],posBtn[1]))

    def drawButtons(self):
        self.drawButtonsGo()
        self.__btnSettings.draw()

    def drawButtonsGo(self):
        self.__btnHumanGo.draw()
        self.__btnBotGo.draw()
        self.__btnOnLineGo.draw()

    def updateButtons(self,event):
        self.updateButtonsGo(event)
        self.__btnSettings.update(event)

    def updateButtonsGo(self, event):
        self.__btnHumanGo.update(event)
        self.__btnBotGo.update(event)
        self.__btnOnLineGo.update(event)

    def creatTexts(self):
        self.__colorText = "yellow"
        self.__tTitle = Text(self.__window,"Tic Tac Toe",(90,70),self.__colorText,80)
        self.__tSubTitle = Text(self.__window,"Bienvenue",(180,170),self.__colorText,50)
        self.__tSubTitle.setFont(self.__fonts[2])
        self.__tTitle.setFont(self.__fonts[3])

    def drawTexts(self):
        self.__tTitle.draw()
        self.__tSubTitle.draw()
        self.__tTitle.setColor(self.__colorText)
        self.__tSubTitle.setColor(self.__colorText)

    def refreshView(self,newShared):
        self.__shared = newShared
        self.createBg()
