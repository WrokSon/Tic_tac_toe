import pygame, sys

class GameView:
    def __init__(self,window,imgGrid,imgP1,imgP2,grid):
        self.__imageGrid = imgGrid
        self.__imagePlayer1 = imgP1
        self.__imagePlayer2 = imgP2
        self.__windowTitle = "Tic Tac Toe"
        self.__window = window
        self.__caseClicked = None
        self.__grid = grid
    
    def getCaseClicked(self):
        return self.__caseClicked
    
    def doEvent(self,event):
        if event.type == pygame.QUIT:
            sys.exit(0)
    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.contains(pygame.mouse.get_pos())
    
    def update(self,event):
        self.doEvent(event)
    
    def drawAll(self,symbolPlayer1,symbolPlayer2):
        self.__window.fill("grey")
        pygame.display.set_caption(self.__windowTitle)
        self.drawGrid()
        self.drawAllTokens(symbolPlayer1,symbolPlayer2)
        pygame.display.update() 
    
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
        #print("\n",self.__caseClicked)
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[i])):
                #print(self.__grid[i][j],end=" ")
                if self.__grid[i][j] == symbolPlayer1:
                    self.drawTokensPlayer(self.__imagePlayer1,(j,i))

                if self.__grid[i][j] == symbolPlayer2:
                    self.drawTokensPlayer(self.__imagePlayer2,(j,i))
            #print()
    def drawTokensPlayer(self,imgPlayer,pos):
        imgDim = ((self.__imgGridDim[1]//3)-10,(self.__imgGridDim[1]//3)-10)
        imgPos = ((pos[0]*(self.__imgGridDim[1]//3))+15,(pos[1]*(self.__imgGridDim[1]//3))+65)
        Img = pygame.transform.scale(imgPlayer, imgDim)
        self.__window.blit(Img,imgPos)
        

              
        