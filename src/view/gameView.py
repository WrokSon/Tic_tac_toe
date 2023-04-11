import pygame, sys, os
sys.path.append(os.getcwd())
from ressources.tools import Text, Button

class GameView:
    def __init__(self,common,imgGrid,players,grid):
        self.__common = common
        self.__imageGrid = imgGrid
        self.__player1 = players[0]
        self.__player2 = players[1]
        self.__windowTitle = "Tic Tac Toe | Game"
        self.__window = self.__common["window"]
        self.__fonts = self.__common["fonts"]
        self.__mode = self.__common["mode"]
        self.__caseClicked = None
        self.__grid = grid
        self.__listWinner = []
        self.__currentSymbol = "O"
        self.createAll()

    def getValueBtnRestart(self):
        return self.__btnRestart.isActive()

    def getValueBtnHomeGo(self):
        return self.__btnHomeGo.isActive()
    
    def setValueBtnRestart(self):
        self.__btnRestart.notActive()

    def setValueBtnHomeGo(self):
        self.__btnHomeGo.notActive()

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
        pygame.display.update()

    def createAll(self):
        self.createBg()
        self.createTexts()
        self.createPofiles()
        self.createButtons()

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
        #Versus
        self.__textVS = Text(self.__window,"VS",(550,140),"yellow")
        self.__textVS.setFont(self.__fonts[2])
        #Score
        self.__textScore = Text(self.__window,"",(100,20))
        self.__textScore.setFont(self.__fonts[0])
        #Turn
        self.__textTrun = Text(self.__window,f"Tour : {self.__currentSymbol}",(300,20))
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
    
    def createProfilePlayerX(self):
        self.__positionProfileX = (480,20)
        marge = (110,[i*20 for i in range(4)])
        size = 20
        color = "white"
        self.__tNamePlayerX = Text(self.__window,f"Nom : {self.__player1.getName()}",(self.__positionProfileX[0]+marge[0],self.__positionProfileX[1]+marge[1][0]),color,size)
        self.__tSymbolPlayerX = Text(self.__window,f"Symbole : '{self.__player1.getSymbol()}'",(self.__positionProfileX[0]+marge[0],self.__positionProfileX[1]+marge[1][1]),color,size)
        self.__tPointPlayerX = Text(self.__window,f"Point : {self.__player1.getPoint()}",(self.__positionProfileX[0]+marge[0],self.__positionProfileX[1]+marge[1][2]),color,size)
        self.__tNbGamePlayedX = Text(self.__window,f"Parties total : {self.__player1.getNbGamePlayed()}",(self.__positionProfileX[0]+marge[0],self.__positionProfileX[1]+marge[1][3]),color,size)
    
    def drawProfilePlayerX(self):
        pygame.draw.rect(self.__window,"black",[(self.__positionProfileX[0]-10,self.__positionProfileX[1]-10),(235,120)])
        Img = pygame.transform.scale(self.__player1.getProfileImg(), (100,100))
        self.__window.blit(Img,self.__positionProfileX)
        self.__tNamePlayerX.draw()
        self.__tPointPlayerX.draw()
        self.__tSymbolPlayerX.draw()
        self.__tNbGamePlayedX.draw()
        self.__tPointPlayerX.setText(f"Point : {self.__player1.getPoint()}")
        self.__tNbGamePlayedX.setText(f"Parties total : {self.__player1.getNbGamePlayed()}")
    
    def createProfilePlayerO(self):
        self.__positionProfileO = (480,200)
        marge = (110,[i*20 for i in range(4)])
        size = 20
        color = "white"
        self.__tNamePlayerO = Text(self.__window,f"Nom : {self.__player2.getName()}",(self.__positionProfileO[0]+marge[0],self.__positionProfileO[1]+marge[1][0]),color,size)
        self.__tSymbolPlayerO = Text(self.__window,f"Symbole : '{self.__player2.getSymbol()}'",(self.__positionProfileO[0]+marge[0],self.__positionProfileO[1]+marge[1][1]),color,size)
        self.__tPointPlayerO = Text(self.__window,f"Point : {self.__player2.getPoint()}",(self.__positionProfileO[0]+marge[0],self.__positionProfileO[1]+marge[1][2]),color,size)
        self.__tNbGamePlayedO = Text(self.__window,f"Parties total : {self.__player2.getNbGamePlayed()}",(self.__positionProfileO[0]+marge[0],self.__positionProfileO[1]+marge[1][3]),color,size)
    
    def drawProfilePlayerO(self):
        pygame.draw.rect(self.__window,"black",[(self.__positionProfileO[0]-10,self.__positionProfileO[1]-10),(235,120)])
        Img = pygame.transform.scale(self.__player2.getProfileImg(), (100,100))
        self.__window.blit(Img,self.__positionProfileO)
        self.__tNamePlayerO.draw()
        self.__tPointPlayerO.draw()
        self.__tSymbolPlayerO.draw()
        self.__tNbGamePlayedO.draw()
        self.__tPointPlayerO.setText(f"Point : {self.__player2.getPoint()}")
        self.__tNbGamePlayedO.setText(f"Parties total : {self.__player2.getNbGamePlayed()}")

    def drawProfile(self):
        self.drawProfilePlayerX()
        self.drawProfilePlayerO()

    def createPofiles(self):
        self.createProfilePlayerX()
        self.createProfilePlayerO()
              
    def createButtons(self):
        self.__btnRestart = Button(self.__window,"restart",position=(550,340))
        self.__btnHomeGo = Button(self.__window,"Home",position=(400,340))

    def drawButtons(self):
        self.__btnRestart.draw()
        self.__btnHomeGo.draw()

    def updateButtons(self,event):
        self.__btnRestart.update(event)
        self.__btnHomeGo.update(event)

    def createBg(self):
        bgImg = self.__common["bg"]
        self.__imgBg = pygame.transform.scale(bgImg, pygame.display.get_surface().get_size())

