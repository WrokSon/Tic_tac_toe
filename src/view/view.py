from abc import ABC, abstractmethod

class View(ABC):

    @abstractmethod
    def createAll(self):
        pass
    
    @abstractmethod
    def drawAll(self):
       pass

    @abstractmethod
    def update(self,event):
        pass

    @abstractmethod
    def createBg(self):
        pass

    @abstractmethod
    def refreshView(self,newShared):
        pass
