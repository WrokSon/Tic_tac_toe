import pygame, sys, os
sys.path.append(os.getcwd())

class Player:
    fistPlayer = True
    
    def __init__(self,name,point=0,nbGamePlayed=0):
        self.__name = name
        self.__point = point
        self.__nbGamePlayed = nbGamePlayed     
        if Player.fistPlayer:
            Player.fistPlayer = not Player.fistPlayer
            self.__symbol = "O" 
            self.__color = "red"
        else:
            self.__symbol = "X"
            Player.fistPlayer = not Player.fistPlayer
            self.__color = "blue"
        self.__profileImg = pygame.image.load(f"src/ressources/images/profile/profilePlayer{self.__symbol}.jpg")
        self.__image = pygame.image.load(f"src/ressources/images/game/player{self.__symbol}.jpg")
        self.__imageWin = pygame.image.load(f"src/ressources/images/game/player{self.__symbol}win.jpg")
    
    #Getters and Setters
    def getName(self):
        return self.__name
    
    def setName(self,newName):
        self.__name = newName
    
    def getPoint(self):
        return self.__point
    
    def setPoint(self,newPoint):
        self.__point = newPoint

    def getNbGamePlayed(self):
        return self.__nbGamePlayed
    
    def setNbGamePlayed(self,newNbGamePlayed):
        self.__nbGamePlayed = newNbGamePlayed
    
    def getProfileImg(self):
        return self.__profileImg
    
    def setProfileImg(self, newProfile):
        self.__profileImg = newProfile
    
    def getImg(self):
        return self.__image
    
    def getImgWin(self):
        return self.__imageWin
    
    def getSymbol(self):
        return self.__symbol
    
    def getColor(self):
        return self.__color
    
    def setColor(self,newColor):
        self.__color = newColor

    #Methods  
    def addPoint(self,point=1):
        self.__point += point
    
    def addNbGamePlayed(self,nbGame=1):
        self.__nbGamePlayed += nbGame
            
     