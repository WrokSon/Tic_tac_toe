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
            self.drawTokens()
            sys.exit(0)
        
        elif event.type == pygame.VIDEORESIZE:
            size = [event.w,event.h]
            if event.w <= 500:
                size[0] = 500
                
            if event.h <= 400:
                size[1] = 400
            pygame.display.set_mode(size, pygame.RESIZABLE)
    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.contains(pygame.mouse.get_pos())
            #print(f"click:{pygame.mouse.get_pos()} dim:{self.__imgGridDim} pos:{self.__imgGridPos}")
    
    def update(self,event):
        self.drawAll()
        self.doEvent(event)
    
    def drawAll(self):
        self.__dimensionWindow = pygame.display.get_surface().get_size()
        self.__dimWinP =(self.__dimensionWindow[0] // 100, self.__dimensionWindow[1] // 100)
        self.__window.fill("grey")
        pygame.display.set_caption(self.__windowTitle)
        self.drawGrid()
    
    def contains(self,posCkick):
        if posCkick[0] >= self.__imgGridPos[0] and posCkick[0] <= self.__imgGridPos[0] + self.__imgGridDim[0]:
            if  posCkick[1] >= self.__imgGridPos[1] and posCkick[1] <= self.__imgGridPos[1] + self.__imgGridDim[1]:
                self.__caseClicked = (posCkick[1]//((self.__imgGridDim[1]//3)+60),posCkick[0]//((self.__imgGridDim[0]//3)+20))
        
    def drawGrid(self):
        self.__imgGridDim = (45*self.__dimWinP[0],60*self.__dimWinP[1])
        self.__imgGridPos = (5*self.__dimWinP[0],20*self.__dimWinP[1])
        self.__gridImg = pygame.transform.scale(self.__imageGrid, self.__imgGridDim)
        self.__window.blit(self.__gridImg,self.__imgGridPos)
  
    def drawTokens(self):
        for elemt in self.__grid:
            for case in elemt:
                print(case,end=" ")
            print()
              
        