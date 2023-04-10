import pygame, sys, os
sys.path.append(os.getcwd())
from ressources.tools import Text

class GameView:
    def __init__(self,window,imgGrid,players,grid):
        self.__imageGrid = imgGrid
        self.__player1 = players[0]
        self.__player2 = players[1]
        self.__windowTitle = "Tic Tac Toe"
        self.__window = window
        self.__caseClicked = None
        self.__grid = grid
        self.createAll()
    
    def getCaseClicked(self):
        return self.__caseClicked

    def doEvent(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.contains(pygame.mouse.get_pos())
    
    def update(self,event):
        self.doEvent(event)
    
    def drawAll(self,symbolPlayer1,symbolPlayer2):
        self.__window.fill("grey")
        pygame.display.set_caption(self.__windowTitle)
        self.drawGrid()
        self.drawAllTokens(symbolPlayer1,symbolPlayer2)
        self.drawTexts()
        self.drawProfile()
        pygame.display.update()

    def createAll(self):
        self.createTexts()
        self.createPofiles()


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
        self.__imgGridPos = (10,60)
        self.__gridImg = pygame.transform.scale(self.__imageGrid, self.__imgGridDim)
        self.__window.blit(self.__gridImg,self.__imgGridPos)
  
    def drawAllTokens(self,symbolPlayer1,symbolPlayer2):
        #print("\n")
        grid = self.__grid.getMatrix()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                #print(self.__grid[i][j],end=" ")
                if grid[i][j] == symbolPlayer1:
                    self.drawTokensPlayer(self.__player1.getImg(),(j,i))

                if grid[i][j] == symbolPlayer2:
                    self.drawTokensPlayer(self.__player2.getImg(),(j,i))
            #print()
    def drawTokensPlayer(self,imgPlayer,pos):
        imgDim = ((self.__imgGridDim[1]//3)-10,(self.__imgGridDim[1]//3)-10)
        imgPos = ((pos[0]*(self.__imgGridDim[1]//3))+15,(pos[1]*(self.__imgGridDim[1]//3))+65)
        Img = pygame.transform.scale(imgPlayer, imgDim)
        self.__window.blit(Img,imgPos)

    def createTexts(self):
        self.__textScore = Text(self.__window,"",(100,20))
        self.__textScore.setFont("src/ressources/fonts/full_pack_2025/full Pack 2025.ttf")

    def drawTexts(self):
        pos = (80,10)
        dimBg = (150,50)
        pygame.draw.rect(self.__window,"yellow",[pos[0],pos[1],dimBg[0],dimBg[1]])
        self.__textScore.setText(f'{self.__player1.getPoint()} - {self.__player2.getPoint()}')
        self.__textScore.draw()
    
    def createProfilePlayerX(self):
        self.__positionProfileX = (450,30)
        marge = (110,[i*20 for i in range(3)])
        size = 20
        color = "blue"
        self.__tNamePlayerX = Text(self.__window,f"Name : {self.__player1.getName()}",(self.__positionProfileX[0]+marge[0],self.__positionProfileX[1]+marge[1][0]),color,size)
        self.__tPointPlayerX = Text(self.__window,f"Point : {self.__player1.getPoint()}",(self.__positionProfileX[0]+marge[0],self.__positionProfileX[1]+marge[1][1]),color,size)
        self.__tSymbolPlayerX = Text(self.__window,f"Symbol : '{self.__player1.getSymbol()}'",(self.__positionProfileX[0]+marge[0],self.__positionProfileX[1]+marge[1][2]),color,size)
    
    def drawProfilePlayerX(self):
        pygame.draw.rect(self.__window,"black",[(self.__positionProfileX[0]-10,self.__positionProfileX[1]-10),(230,120)])
        Img = pygame.transform.scale(self.__player1.getProfileImg(), (100,100))
        self.__window.blit(Img,self.__positionProfileX)
        self.__tNamePlayerX.draw()
        self.__tPointPlayerX.draw()
        self.__tSymbolPlayerX.draw()
        self.__tPointPlayerX.setText(f"Point : {self.__player1.getPoint()}")
    
    def createProfilePlayerO(self):
        self.__positionProfileO = (450,200)
        marge = (110,[i*20 for i in range(3)])
        size = 20
        color = "blue"
        self.__tNamePlayerO = Text(self.__window,f"Name : {self.__player2.getName()}",(self.__positionProfileO[0]+marge[0],self.__positionProfileO[1]+marge[1][0]),color,size)
        self.__tPointPlayerO = Text(self.__window,f"Point : {self.__player2.getPoint()}",(self.__positionProfileO[0]+marge[0],self.__positionProfileO[1]+marge[1][1]),color,size)
        self.__tSymbolPlayerO = Text(self.__window,f"Symbol : '{self.__player2.getSymbol()}'",(self.__positionProfileO[0]+marge[0],self.__positionProfileO[1]+marge[1][2]),color,size)
    
    def drawProfilePlayerO(self):
        pygame.draw.rect(self.__window,"black",[(self.__positionProfileO[0]-10,self.__positionProfileO[1]-10),(230,120)])
        Img = pygame.transform.scale(self.__player2.getProfileImg(), (100,100))
        self.__window.blit(Img,self.__positionProfileO)
        self.__tNamePlayerO.draw()
        self.__tPointPlayerO.draw()
        self.__tSymbolPlayerO.draw()
        self.__tPointPlayerO.setText(f"Point : {self.__player2.getPoint()}")

    def drawProfile(self):
        self.drawProfilePlayerX()
        self.drawProfilePlayerO()

    def createPofiles(self):
        self.createProfilePlayerX()
        self.createProfilePlayerO()
              
        