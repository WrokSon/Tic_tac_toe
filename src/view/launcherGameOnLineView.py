import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from view.view import View
from resources.tools.toolsDisplayable import Text, Button, TextInputBox
pygame.init()

class LauncherGameOnLineView(View):
    def __init__(self,shared):
        self.__shared = shared
        self.__windowTitle = "Tic Tac Toe | Salon pour jouer en ligne"
        self.__window = self.__shared["window"]
        self.__fonts = self.__shared["fonts"]
        self.__viewJoin = True
        self.__isConnected = False
        self.createAll()
    
    def getValueBtnHome(self):
        return self.__btnHomeGo.isActive()
    
    def getValueBtnStart(self):
        return self.__btnStartGo.isActive()
    
    def getValueBtnConnect(self):
        return self.__btnConnectGo.isActive()

    def getValueBtnTypOfConnection(self):
        return self.__btnTypOfConnection.isActive()

    def getTextBtnTypOfConnection(self):
        return self.__btnTypOfConnection.getText()
    
    def getValueBtnMessagePlayer(self):
        return self.__btnMessagePlayer.isActive()

    def getValueTIBIPPlayer2(self):
        return self.__tIBIPPlayer2.getText()

    def getValueTIBMessagePlayer(self):
        return self.__tIBMessagePlayer.getText()

    def setValueViewJoin(self):
        self.__viewJoin = not self.__viewJoin

    def setValueIsConnected(self):
        self.__isConnected = not self.__isConnected

    def setValueBtnHome(self):
        self.__btnHomeGo.notActive()
    
    def setValueBtnStart(self):
        self.__btnStartGo.notActive()
    
    def setValueBtnTypOfConnection(self):
        self.__btnTypOfConnection.notActive()
    
    def setTextBtnTypOfConnection(self,value):
        self.__btnTypOfConnection.setText(value)

    def setValueBtnConnect(self):
        self.__btnConnectGo.notActive()

    def setValueBtnMessagePlayer(self):
        self.__btnMessagePlayer.notActive()

    def setValueTIBMessagePlayer(self):
        self.__tIBMessagePlayer.setText("")

    def createAll(self):
        self.__posElemntsX = [100,350]
        self.__posElemntsY = [70,150,220,245,330]
        self.createBg()
        self.createButtons()
        self.createTexts()
        self.createTextInputBox()
        pygame.display.update()
    
    def createTexts(self):
        self.__colorText = "black"
        self.__tTitle = Text(self.__window,"Salle d'attente",(250,20))
        self.__tIPPlayer2 = Text(self.__window,"IP du salon : ",(self.__posElemntsX[0],self.__posElemntsY[2]),size=17)
        self.createTextConnected()
        self.createTextsServer()
        self.setFontText()

    def createTextConnected(self):
        margeX = [30,100]
        nameP1 = "Nom du Joueur 1 : "+ self.__shared["NamePlayer1"]
        nameP2 = "Nom du Joueur 2 : "+ self.__shared["NamePlayer2"]
        sizeText = 15
        margeY = 30
        color = "white"
        self.__tNamePlayer1 = Text(self.__window,nameP1,(self.__posElemntsX[0]-margeX[0],self.__posElemntsY[0]),size=sizeText)
        self.__tNamePlayer2 = Text(self.__window,nameP2,(self.__posElemntsX[1]+margeX[0],self.__posElemntsY[0]),size=sizeText)
        
        self.createTextsMessage(margeX, margeY, color)

    def createTextsMessage(self, margeX, margeY, color):
        self.__tMessageName1 = Text(self.__window,self.__shared["NamePlayer1"],(self.__posElemntsX[0]-margeX[0],self.__posElemntsY[3]),"red")
        self.__tMessageName2 = Text(self.__window,self.__shared["NamePlayer2"],(self.__posElemntsX[0]-margeX[0],self.__posElemntsY[3]+margeY),"blue")
        self.__tMessagePlayer1 = Text(self.__window,": Bienvenue",(self.__posElemntsX[0]+margeX[1],self.__posElemntsY[3]),color)
        self.__tMessagePlayer2 = Text(self.__window,": Bienvenue",(self.__posElemntsX[0]+margeX[1],self.__posElemntsY[3]+margeY),color)

    def createTextsServer(self):
        self.__tMyIP = Text(self.__window,self.__shared["IpAddrClient"],(self.__posElemntsX[1]-170,self.__posElemntsY[2]-30),"white",size=50)
        self.__tMessageServerLisening = Text(self.__window,"En attente de connexion...",(self.__posElemntsX[1]+100,self.__posElemntsY[4]+30),size=17)

    def setFontText(self):
        self.__tTitle.setFont(self.__fonts[1])
        self.__tIPPlayer2.setFont(self.__fonts[2])
        self.__tMyIP.setFont(self.__fonts[3])
        self.__tMessageServerLisening.setFont(self.__fonts[1])
        self.__tNamePlayer1.setFont(self.__fonts[1])
        self.__tNamePlayer2.setFont(self.__fonts[1])

    def createButtons(self):
        self.__btnTypOfConnection = Button(self.__window,"REJOINDRE",position=(240,self.__posElemntsY[0]),dimension=(250,50))
        self.__btnHomeGo = Button(self.__window,"[H]",position=(10,self.__posElemntsY[4]))
        self.__btnStartGo = Button(self.__window,"JOUER",position=(570,self.__posElemntsY[4]))
        self.__btnConnectGo = Button(self.__window,"CONNECTER",position=(510,self.__posElemntsY[4]),dimension=(200,50))
        self.__btnMessagePlayer = Button(self.__window,"ENVOYER",position=(self.__posElemntsX[1]-60,self.__posElemntsY[1]+15),dimension=(180,50))

    def createTextInputBox(self):
        self.__tIBIPPlayer2 = TextInputBox(self.__window,(self.__posElemntsX[1],self.__posElemntsY[2]-10),maximum=15)
        self.__tIBMessagePlayer = TextInputBox(self.__window,(self.__posElemntsX[0]+15,self.__posElemntsY[1]-40),(500,50),30)


    def drawAll(self):
        self.__window.blit(self.__imgBg,(0,0))
        pygame.display.set_caption(self.__windowTitle)
        self.drawTexts()
        self.drawButtons()
        self.drawTextInputBox()
        pygame.display.update()

    def drawTexts(self):
        color = "white"
        self.__tTitle.draw() 
        self.__tTitle.setColor(self.__colorText)
        if not self.__isConnected : 
            self.drawTextsIsNotConnected(color)     
        else:
            pygame.draw.rect(self.__window,color,[(50,50),(630,270)])
            pygame.draw.rect(self.__window,"black",[(65,self.__posElemntsY[3]-15),(600,80)])
            self.__tNamePlayer1.draw()
            self.__tNamePlayer2.draw()
            self.__tIBMessagePlayer.draw()
            self.__tMessagePlayer1.draw()
            self.__tMessagePlayer2.draw()
            self.__tMessageName1.draw()
            self.__tMessageName2.draw()

    def drawTextsIsNotConnected(self, color):
        if self.__viewJoin : 
            pygame.draw.rect(self.__window,color,[(self.__posElemntsX[0]-20,self.__posElemntsY[2]-10),(220,50)])
            self.__tIPPlayer2.draw()
        else:
            pygame.draw.rect(self.__window,"black",[(self.__posElemntsX[1]-200,self.__posElemntsY[1]),(460,140)])
            self.__tMyIP.draw() 
            self.__tMessageServerLisening.draw()
            self.__tMessageServerLisening.setColor(self.__colorText)

    def drawButtons(self):
        self.__btnHomeGo.draw()
        if not self.__viewJoin and self.__isConnected : self.__btnStartGo.draw()
        if not self.__isConnected : self.__btnTypOfConnection.draw()
        if self.__viewJoin and not self.__isConnected : self.__btnConnectGo.draw()
        if self.__isConnected : self.__btnMessagePlayer.draw()

    def drawTextInputBox(self):
        if self.__viewJoin and not self.__isConnected : self.__tIBIPPlayer2.draw()

    def update(self,event):
        self.updateButtons(event)
        self.updateTextInputBox(event)
        self.doEvent(event)

    def updateButtons(self, event):
        self.__btnHomeGo.update(event)
        if not self.__viewJoin and self.__isConnected : self.__btnStartGo.update(event)
        if not self.__isConnected and not self.__isConnected : self.__btnTypOfConnection.update(event)
        if self.__viewJoin and not self.__isConnected : self.__btnConnectGo.update(event)
        if self.__isConnected : self.__btnMessagePlayer.update(event)

    def updateTextInputBox(self,event):
        if self.__viewJoin and not self.__isConnected : self.__tIBIPPlayer2.update(event)
        if self.__isConnected : self.__tIBMessagePlayer.update(event)

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
        self.__isConnected = self.__shared["isConnected"]
        self.setTexts()
        self.createBg()

    def setTexts(self):
        nameP1 = self.__shared["NamePlayer1"]
        nameP2 = self.__shared["NamePlayer2"]
        self.__tIBIPPlayer2.setText(self.__shared["IpAddrServer"])
        self.__tNamePlayer1.setText("Nom du Joueur 1 : " +nameP1)
        self.__tNamePlayer2.setText("Nom du Joueur 2 : " +nameP2)
        self.__tMessageName1.setText(nameP1)
        self.__tMessageName2.setText(nameP2)
        self.__tMessagePlayer1.setText(": "+self.__shared["msgPlayers"][0])
        self.__tMessagePlayer2.setText(": "+self.__shared["msgPlayers"][1])

