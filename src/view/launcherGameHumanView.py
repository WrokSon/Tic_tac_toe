import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from view.view import View
from resources.tools.toolsDisplayable import Text, Button, TextInputBox

pygame.init()

class LauncherGameHumanView(View):
    def __init__(self,shared):
        self.__shared = shared
        self.__windowTitle = "Tic Tac Toe | Salon pour un 1V1"
        self.__window = self.__shared["window"]
        self.__fonts = self.__shared["fonts"]
        self.__icons = self.__shared["icons"]
        self.createAll()
    
    def getValueBtnHome(self):
        return self.__btnHomeGo.isActive()
    
    def getValueBtnStart(self):
        return self.__btnStartGo.isActive()
    
    def getValueTIBPlayer1(self):
        return self.__tIBPlayer1.getText()
    
    def getValueTIBPlayer2(self):
        return self.__tIBPlayer2.getText()

    def setValueBtnHome(self):
        self.__btnHomeGo.notActive()
    
    def setValueBtnStart(self):
        self.__btnStartGo.notActive()
    
    def setValueTIBPlayer1(self):
        self.__tIBPlayer1.setText("")
    
    def setValueTIBPlayer2(self):
        self.__tIBPlayer2.setText("")

    def createAll(self):
        self.__posElemntsX = [30,390]
        self.__posElemntsY = [120,200]
        self.createBg()
        self.createButtons()
        self.createTexts()
        self.createTextInputBox()
        pygame.display.update()
    
    def createTexts(self):
        marge = 50
        self.__colorText = "black"
        sizeText = 17
        self.__tTitle = Text(self.__window,"Salle d'attente",(250,20))
        self.__tNamePlayer1 = Text(self.__window,"Nom du joueur 1",(self.__posElemntsX[0]+marge,self.__posElemntsY[0]),"red",sizeText)
        self.__tNamePlayer2 = Text(self.__window,"Nom du joueur 2",(self.__posElemntsX[1]+marge,self.__posElemntsY[0]),"blue",sizeText)
        self.__tTitle.setFont(self.__fonts[1])
        self.__tNamePlayer1.setFont(self.__fonts[2])
        self.__tNamePlayer2.setFont(self.__fonts[2])

    def createButtons(self):
        btnsPosY = 330
        self.__btnHomeGo = Button(self.__window,"[H]",position=(10,btnsPosY))
        self.__btnStartGo = Button(self.__window,"JOUER",position=(570,btnsPosY))

        self.__btnHomeGo.setIcon(self.__icons[3])

    def createTextInputBox(self):
        self.__tIBPlayer1 = TextInputBox(self.__window,(self.__posElemntsX[0],self.__posElemntsY[1]))
        self.__tIBPlayer2 = TextInputBox(self.__window,(self.__posElemntsX[1],self.__posElemntsY[1]))
        self.__tIBPlayer1.setText(self.__shared["NamePlayer1"])
        self.__tIBPlayer2.setText(self.__shared["NamePlayer2"])


    def drawAll(self):
        self.__window.blit(self.__imgBg,(0,0))
        pygame.display.set_caption(self.__windowTitle)
        self.drawButtons()
        self.drawTexts()
        self.drawTextInputBox()
        pygame.display.update()

    def drawTexts(self):
        self.__tTitle.draw()
        dimension = (220,50)
        margeX = 35
        margeY = 10
        pygame.draw.rect(self.__window,"white",[(self.__posElemntsX[0]+margeX,self.__posElemntsY[0]-margeY),dimension])
        pygame.draw.rect(self.__window,"white",[(self.__posElemntsX[1]+margeX,self.__posElemntsY[0]-margeY),dimension])
        self.__tNamePlayer1.draw()
        self.__tNamePlayer2.draw()

        self.__tTitle.setColor(self.__colorText)

    def drawButtons(self):
        self.__btnHomeGo.draw()
        self.__btnStartGo.draw()

    def drawTextInputBox(self):
        self.__tIBPlayer1.draw()
        self.__tIBPlayer2.draw()

    def update(self,event):
        self.updateButtons(event)
        self.updateTextInputBox(event)
        self.doEvent(event)

    def updateButtons(self, event):
        self.__btnHomeGo.update(event)
        self.__btnStartGo.update(event)
    
    def updateTextInputBox(self,event):
        self.__tIBPlayer1.update(event)
        self.__tIBPlayer2.update(event)
    
    def doEvent(self,event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if self.__colorText == "White":
                self.__colorText = "black"
            else:
                self.__colorText = "White"

    def createBg(self):
        bgImg = pygame.image.load(self.__shared["bg"])
        self.__imgBg = pygame.transform.scale(bgImg, pygame.display.get_surface().get_size())

    def refreshView(self,newShared):
        self.__shared = newShared
        self.__tIBPlayer1.setText(self.__shared["NamePlayer1"])
        self.__tIBPlayer2.setText(self.__shared["NamePlayer2"])
        self.createBg()
