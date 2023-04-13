import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from view.view import View
from resources.tools.toolsDisplayable import Text, Button, TextInputBox

pygame.init()

class LauncherGameSoloView(View):
    def __init__(self,shared):
        self.__shared = shared
        self.__windowTitle = "Tic Tac Toe | Salon pour jouer tout seul"
        self.__window = self.__shared["window"]
        self.__fonts = self.__shared["fonts"]
        self.createAll()
    
    def getValueBtnHome(self):
        return self.__btnHomeGo.isActive()
    
    def getValueBtnStart(self):
        return self.__btnStartGo.isActive()
    
    def getValueBtnDificulty(self):
        return self.__btnDificulty.isActive()
    
    def getValueTIBPlayer1(self):
        return self.__tIBPlayer.getText()
    
    def getTextBtnDificulty(self):
        return self.__btnDificulty.getText()

    def setValueBtnHome(self):
        self.__btnHomeGo.notActive()
    
    def setValueBtnStart(self):
        self.__btnStartGo.notActive()

    def setValueBtnDificulty(self):
        self.__btnDificulty.notActive()
    
    def setTextBtnDificulty(self,newText):
        self.__btnDificulty.setText(newText)
    
    def setValueTIBPlayer1(self):
        self.__tIBPlayer.setText("")

    def createAll(self):
        self.__posElemntsX = [30,480]
        self.__posElemntsY = [120,200]
        self.createBg()
        self.createButtons()
        self.createTexts()
        self.createTextInputBox()
        pygame.display.update()
    
    def createTexts(self):
        self.__colorText = "black"
        self.__tTitle = Text(self.__window,"Salle d'attente",(250,20))
        self.__tNamePlayer = Text(self.__window,"Nom du joueur",(self.__posElemntsX[0]+50,self.__posElemntsY[0]),"red",17)
        self.__tDificulty = Text(self.__window,"Niveau",(self.__posElemntsX[1]+30,self.__posElemntsY[0]),self.__colorText,35)
        self.__tTitle.setFont(self.__fonts[1])
        self.__tNamePlayer.setFont(self.__fonts[2])
        self.__tDificulty.setFont(self.__fonts[1])

    def createButtons(self):
        btnsPosY = 330
        self.__btnHomeGo = Button(self.__window,"[H]",position=(10,btnsPosY))
        self.__btnStartGo = Button(self.__window,"JOUER",position=(570,btnsPosY))
        self.__btnDificulty = Button(self.__window,self.__shared["difficulty"],position=(self.__posElemntsX[1],self.__posElemntsY[1]-20),dimension=(200,50))

    def createTextInputBox(self):
        self.__tIBPlayer = TextInputBox(self.__window,(self.__posElemntsX[0],self.__posElemntsY[1]))
        self.__tIBPlayer.setText(self.__shared["NamePlayer1"])

    def drawAll(self):
        self.__window.blit(self.__imgBg,(0,0))
        pygame.display.set_caption(self.__windowTitle)
        self.drawButtons()
        self.drawTexts()
        self.drawTextInputBox()
        pygame.display.update()

    def drawTexts(self):
        self.__tTitle.draw()
        pygame.draw.rect(self.__window,"white",[(self.__posElemntsX[0]+30,self.__posElemntsY[0]-10),(220,50)])
        self.__tNamePlayer.draw()
        self.__tDificulty.draw()

        self.__tTitle.setColor(self.__colorText)
        self.__tDificulty.setColor(self.__colorText)

    def drawButtons(self):
        self.__btnHomeGo.draw()
        self.__btnStartGo.draw()
        self.__btnDificulty.draw()

    def drawTextInputBox(self):
        self.__tIBPlayer.draw()

    def update(self,event):
        self.updateButtons(event)
        self.updateTextInputBox(event)
        self.doEvent(event)

    def updateButtons(self, event):
        self.__btnHomeGo.update(event)
        self.__btnStartGo.update(event)
        self.__btnDificulty.update(event)
    
    def updateTextInputBox(self,event):
        self.__tIBPlayer.update(event)

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
        self.__tIBPlayer.setText(self.__shared["NamePlayer1"])
        self.__btnDificulty.setText(self.__shared["difficulty"])
        self.createBg()
