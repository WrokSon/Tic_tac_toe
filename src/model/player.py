class Player:
    fistPlayer = True
    
    def __init__(self,name,point=0):
        self.__name = name
        self.__point = point
        self.__synbol = "O" if Player.fistPlayer else "X"
        self.__profile = 0 #a venir (image)
    
    #Getters and Setters
    def getName(self):
        return self.__name
    
    def setName(self,newName):
        self.__name = newName
    
    def getPoint(self):
        return self.__point
    
    def setPoint(self,newPoint):
        self.__point = newPoint
    
    def getProfile(self):
        return self.__profile
    
    def setProfile(self, newProfile):
        self.__profile = newProfile
        
    #Methods
    
    def addPoint(self,point=1):
        self.__point += point
            
     