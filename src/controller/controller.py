from abc import ABC, abstractmethod

class Controller(ABC):

    @abstractmethod
    def action(self,event):
        pass

    @abstractmethod
    def update(self,sharedUpdate):
        pass

    @abstractmethod
    def run(self):
        pass