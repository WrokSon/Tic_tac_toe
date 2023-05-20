import pygame, sys, os
sys.path.append(os.getcwd())
from view.view import View
from resources.tools.toolsDisplayable import Text, Button

class GameView(View):
    def __init__(self,shared,imgGrid,players,grid):
        self.__shared = shared
        self.__imageGrid = imgGrid
        self.__player1 = players[0]
        self.__player2 = players[1]
        self.__windowTitle = "Tic Tac Toe | Jeu"
        self.__window = self.__shared["window"]
        self.__fonts = self.__shared["fonts"]
        self.__icons = self.__shared["icons"]
        self.__mode = self.__shared["mode"]
        self.__caseClicked = None
        self.__grid = grid
        self.__listWinner = []
        self.__currentSymbol = "O"
        self.createAll()

    def getValueBtnRestart(self):
        return self.__btnRestart.isActive()

    def getValueBtnHomeGo(self):
        return self.__btnHomeGo.isActive()
    
    def getValueBtnSettings(self):
        return self.__btnSettingsGo.isActive()

    def getValueBtnSaveFile(self):
        return self.__btnSaveFile.isActive()

    def setValueBtnRestart(self):
        self.__btnRestart.notActive()

    def setValueBtnHomeGo(self):
        self.__btnHomeGo.notActive()

    def setValueBtnSettings(self):
        self.__btnSettingsGo.notActive()

    def setValueBtnSaveFile(self):
        self.__btnSaveFile.notActive()

    def setListWinner(self,newList):
        self.__listWinner = newList

    def setCurrentSymbol(self, newCurrentSymbol):
        self.__currentSymbol = newCurrentSymbol

    def getCaseClicked(self):
        return self.__caseClicked
    
    def setCaseClicked(self, newValue):
        self.__caseClicked = newValue

    def doEvent(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.__listWinner == []:
            self.contains(pygame.mouse.get_pos())

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if self.__colorTurnText == "white":
                self.__colorTurnText = "black"
            else:
                self.__colorTurnText = "white"
   
    def update(self,event):
        self.doEvent(event)
        self.updateButtons(event)
    
    def drawAll(self):
        self.__window.blit(self.__imgBg,(0,0))
        pygame.display.set_caption(self.__windowTitle)
        self.drawGrid()
        self.drawAllTokens()
        self.drawTexts()
        self.drawProfile()
        self.drawButtons()
        self.drawScoreBar()
        pygame.display.update()

    def createAll(self):
        self.createBg()
        self.createTexts()
        self.createPofiles()
        self.createButtons()
        self.createScoreBar()

    def contains(self,posClick):
        #posClick est la position de la sourie au moment du clique
        if posClick[0] >= self.__imgGridPos[0] and posClick[0] <= self.__imgGridPos[0] + self.__imgGridDim[0]:
            if  posClick[1] >= self.__imgGridPos[1] and posClick[1] <= self.__imgGridPos[1] + self.__imgGridDim[1]:
                #calcul est simple
                #1)on retir la marge da la grille au position de la souris
                #2)on divise (entiere) par la taille de la grille lui meme diviser(entiere) par 3
                self.__caseClicked = ((posClick[0]-self.__imgGridPos[0])//(self.__imgGridDim[0]//3),
                                      (posClick[1]-self.__imgGridPos[1])//(self.__imgGridDim[1]//3))

    def drawGrid(self):
        self.__imgGridDim = (300,300)
        self.__imgGridPos = (10,80)
        self.__gridImg = pygame.transform.scale(self.__imageGrid, self.__imgGridDim)
        self.__window.blit(self.__gridImg,self.__imgGridPos)
  
    def drawAllTokens(self):
        grid = self.__grid.getMatrix()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == self.__player1.getSymbol():
                    if (i,j) in self.__listWinner:
                        self.drawTokensPlayer(self.__player1.getImgWin(),(j,i))
                    else:
                        self.drawTokensPlayer(self.__player1.getImg(),(j,i))

                if grid[i][j] == self.__player2.getSymbol():
                    if (i,j) in self.__listWinner:
                        self.drawTokensPlayer(self.__player2.getImgWin(),(j,i))
                    else:
                        self.drawTokensPlayer(self.__player2.getImg(),(j,i))

    def drawTokensPlayer(self,imgPlayer,pos):
        imgDim = ((self.__imgGridDim[1]//3)-10,(self.__imgGridDim[1]//3)-10)
        imgPos = ((pos[0]*(self.__imgGridDim[1]//3))+15,(pos[1]*(self.__imgGridDim[1]//3))+85)
        Img = pygame.transform.scale(imgPlayer, imgDim)
        self.__window.blit(Img,imgPos)

    def createTexts(self):
        self.__colorTurnText = "black"
        #Versus
        self.__textVS = Text(self.__window,"VS",(550,140),"yellow")
        self.__textVS.setFont(self.__fonts[2])
        #Score
        self.__textScore = Text(self.__window,"",(100,20))
        self.__textScore.setFont(self.__fonts[0])
        #Turn
        self.__textTrun = Text(self.__window,f"Tour : {self.__currentSymbol}",(300,20),self.__colorTurnText)
        self.__textTrun.setFont(self.__fonts[1])

    def drawTexts(self):
        #score
        pos = (80,10)
        dimBg = (150,50)
        pygame.draw.rect(self.__window,"yellow",[pos[0],pos[1],dimBg[0],dimBg[1]])
        self.__textScore.setText(f'{self.__player1.getPoint()} - {self.__player2.getPoint()}')
        self.__textScore.draw()
        #versus
        self.__textVS.draw()
        #tour
        self.__textTrun.draw()
        self.__textTrun.setText(f"Tour : {self.__currentSymbol}")
        self.__textTrun.setColor(self.__colorTurnText)
    
    def createProfilePlayerX(self):
        self.__positionProfileX = (self.__posProfileX,20)
        self.__tNamePlayerX = Text(self.__window,f"Nom : {self.__player1.getName()}",(self.__positionProfileX[0]+self.__margeProfile[0],self.__positionProfileX[1]+self.__margeProfile[1][0]),self.__colorProfileText,self.__profileSize)
        self.__tSymbolPlayerX = Text(self.__window,f"Symbole : '{self.__player1.getSymbol()}'",(self.__positionProfileX[0]+self.__margeProfile[0],self.__positionProfileX[1]+self.__margeProfile[1][1]),self.__colorProfileText,self.__profileSize)
        self.__tPointPlayerX = Text(self.__window,f"Point : {self.__player1.getPoint()}",(self.__positionProfileX[0]+self.__margeProfile[0],self.__positionProfileX[1]+self.__margeProfile[1][2]),self.__colorProfileText,self.__profileSize)
        self.__tNbGamePlayedX = Text(self.__window,f"Parties total : {self.__player1.getNbGamePlayed()}",(self.__positionProfileX[0]+self.__margeProfile[0],self.__positionProfileX[1]+self.__margeProfile[1][3]),self.__colorProfileText,self.__profileSize)
    
    def drawProfilePlayerX(self):
        pygame.draw.rect(self.__window,self.__player1.getColor(),[(self.__positionProfileX[0]-10,self.__positionProfileX[1]-10),self.__dimProfileBg])
        Img = pygame.transform.scale(self.__player1.getProfileImg(), (100,100))
        self.__window.blit(Img,self.__positionProfileX)
        self.__tNamePlayerX.draw()
        self.__tPointPlayerX.draw()
        self.__tSymbolPlayerX.draw()
        self.__tNbGamePlayedX.draw()
        self.__tNamePlayerX.setText(f"Nom : {self.__player1.getName()}")
        self.__tPointPlayerX.setText(f"Point : {self.__player1.getPoint()}")
        self.__tNbGamePlayedX.setText(f"Parties total : {self.__player1.getNbGamePlayed()}")
    
    def createProfilePlayerO(self):
        self.__positionProfileO = (self.__posProfileX,200)
        self.__tNamePlayerO = Text(self.__window,f"Nom : {self.__player2.getName()}",(self.__positionProfileO[0]+self.__margeProfile[0],self.__positionProfileO[1]+self.__margeProfile[1][0]),self.__colorProfileText,self.__profileSize)
        self.__tSymbolPlayerO = Text(self.__window,f"Symbole : '{self.__player2.getSymbol()}'",(self.__positionProfileO[0]+self.__margeProfile[0],self.__positionProfileO[1]+self.__margeProfile[1][1]),self.__colorProfileText,self.__profileSize)
        self.__tPointPlayerO = Text(self.__window,f"Point : {self.__player2.getPoint()}",(self.__positionProfileO[0]+self.__margeProfile[0],self.__positionProfileO[1]+self.__margeProfile[1][2]),self.__colorProfileText,self.__profileSize)
        self.__tNbGamePlayedO = Text(self.__window,f"Parties total : {self.__player2.getNbGamePlayed()}",(self.__positionProfileO[0]+self.__margeProfile[0],self.__positionProfileO[1]+self.__margeProfile[1][3]),self.__colorProfileText,self.__profileSize)
    
    def drawProfilePlayerO(self):
        pygame.draw.rect(self.__window,self.__player2.getColor(),[(self.__positionProfileO[0]-10,self.__positionProfileO[1]-10),self.__dimProfileBg])
        Img = pygame.transform.scale(self.__player2.getProfileImg(), (100,100))
        self.__window.blit(Img,self.__positionProfileO)
        self.__tNamePlayerO.draw()
        self.__tPointPlayerO.draw()
        self.__tSymbolPlayerO.draw()
        self.__tNbGamePlayedO.draw()
        self.__tNamePlayerO.setText(f"Nom : {self.__player2.getName()}")
        self.__tPointPlayerO.setText(f"Point : {self.__player2.getPoint()}")
        self.__tNbGamePlayedO.setText(f"Parties total : {self.__player2.getNbGamePlayed()}")

    def drawProfile(self):
        self.__dimProfileBg = (265,120)
        self.drawProfilePlayerX()
        self.drawProfilePlayerO()

    def createPofiles(self):
        self.__colorProfileText = "black"
        self.__posProfileX = 460
        self.__margeProfile = (110,[i*20 for i in range(4)])
        self.__profileSize = 20
        self.createProfilePlayerX()
        self.createProfilePlayerO()
              
    def createButtons(self):
        btnPosition = [[i*85+290 for i in range(1,5)],340]
        dimBtn = (80,50)
        self.__btnRestart = Button(self.__window,"[R]",position=(btnPosition[0][2],btnPosition[1]),dimension=dimBtn)
        self.__btnHomeGo = Button(self.__window,"[H]",position=(btnPosition[0][1],btnPosition[1]),dimension=dimBtn)
        self.__btnSettingsGo = Button(self.__window,"[S]",position=(btnPosition[0][0],btnPosition[1]),dimension=dimBtn)
        self.__btnSaveFile = Button(self.__window,"\|/",position=(btnPosition[0][3],btnPosition[1]),dimension=dimBtn)
        self.setIconButtons()

    def setIconButtons(self):
        self.__btnSettingsGo.setIcon(self.__icons[0])
        self.__btnSaveFile.setIcon(self.__icons[1])
        self.__btnRestart.setIcon(self.__icons[2])
        self.__btnHomeGo.setIcon(self.__icons[3])

    def drawButtons(self):
        self.__btnRestart.draw()
        self.__btnHomeGo.draw()
        self.__btnSettingsGo.draw()
        self.__btnSaveFile.draw()

    def updateButtons(self,event):
        self.__btnRestart.update(event)
        self.__btnHomeGo.update(event)
        self.__btnSettingsGo.update(event)
        self.__btnSaveFile.update(event)

    def createBg(self):
        bgImg = pygame.image.load(self.__shared["bg"])
        self.__imgBg = pygame.transform.scale(bgImg, pygame.display.get_surface().get_size())

    def createScoreBar(self):
        self.__tScoreBarPlayer1Pos = (330,70)
        self.__tScoreBarPlayer2Pos = (330,310)
        self.__tScoreBarPlayer1 = Text(self.__window,self.__player1.getName(),self.__tScoreBarPlayer1Pos,size=20)
        self.__tScoreBarPlayer2 = Text(self.__window,self.__player2.getName(),self.__tScoreBarPlayer2Pos,size=20)
        self.__tScoreBarPlayer1.setFont(self.__fonts[3])
        self.__tScoreBarPlayer2.setFont(self.__fonts[3])

    def drawScoreBar(self):
        DimBgPlayer = (120,35)
        infoBar = [(350,100),(50,195)]
        self.drawScoreBarPlayers(infoBar)
        pygame.draw.rect(self.__window,"black",infoBar,5)
        pygame.draw.rect(self.__window,self.__player1.getColor(),[(self.__tScoreBarPlayer1Pos[0]-10,self.__tScoreBarPlayer1Pos[1]-10),DimBgPlayer])
        pygame.draw.rect(self.__window,self.__player2.getColor(),[(self.__tScoreBarPlayer2Pos[0]-10,self.__tScoreBarPlayer2Pos[1]-10),DimBgPlayer])
        self.__tScoreBarPlayer1.draw()
        self.__tScoreBarPlayer2.draw()

    def drawScoreBarPlayers(self,infoBar):
        lengthBarPalyer1 = infoBar[1][1]//2
        nbPartGame = self.__player1.getPoint() + self.__player2.getPoint()
        if nbPartGame != 0 : lengthBarPalyer1 = (self.__player1.getPoint()*infoBar[1][1])//nbPartGame
        pygame.draw.rect(self.__window,self.__player2.getColor(),infoBar)
        pygame.draw.rect(self.__window,self.__player1.getColor(),[infoBar[0],(infoBar[1][0],lengthBarPalyer1)])

    def refreshView(self,newShared):
        self.__shared = newShared
        self.createBg()


