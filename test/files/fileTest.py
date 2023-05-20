import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *

pygame.init()

class Button:
    def __init__(self, window, text="Button", hoverColor=(200, 190, 250), color=(220, 220, 220), position=(0, 0),
                 dimension=(140, 50),sizeText = 40):
        self.position = position
        self.__dimension = dimension
        self.__sizeText = sizeText
        self.__window = window
        self.__text = text
        self.__active = False
        self.__hoverColorBg = hoverColor
        self.__colorBg = color
        self.__colorNormal = color
        self.__colorText = "black"
        self.__icon = None
        self.__typText = True
        self.rect = pygame.Rect(self.position, self.__dimension)

    def getText(self):
        return self.__text

    def setText(self,newText):
        self.__text = newText

    def setIcon(self,newIcon):
        self.__typText = False
        img = pygame.image.load(newIcon)
        self.__icon = pygame.transform.scale(img,(40,40))

    def isActive(self):
        return self.__active

    def notActive(self):
        self.__active = False
        self.__colorText = "black"
        self.__colorBg = self.__colorNormal

    def draw(self):
        self.drawBg()
        if self.__typText : self.drawText()
        else : self.drawIcon()

    def drawIcon(self):
        if self.__icon != None:
            self.__window.blit(self.__icon,self.__icon.get_rect(center=self.rect.center))
        else:
            self.__text = "fail"

    def drawText(self):
        font = pygame.font.Font(None, self.__sizeText)
        text = font.render(self.__text, True, self.__colorText)
        self.__window.blit(text, text.get_rect(center=self.rect.center))

    def contains(self, pos):
        if self.position[0] <= pos[0] <= self.position[0] + self.__dimension[0]:
            if self.position[1] <= pos[1] <= self.position[1] + self.__dimension[1]:
                return True
        return False

    def drawBg(self):
        pygame.draw.rect(self.__window, self.__colorBg, self.rect, 0)
        pygame.draw.rect(self.__window, "black", self.rect, 3)

    def update(self, event):
        if self.contains(pygame.mouse.get_pos()):
            self.__colorText = "white"
            self.__colorBg = self.__hoverColorBg
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.__active = True
        else:
            self.notActive()
        self.draw()

    def changePos(self, pos):
        self.position = pos
        self.rect = pygame.Rect(self.position, self.__dimension)

window = pygame.display.set_mode((400,400))
b = Button(window,"test",position=(150,150))
b.setIcon("test/files/iconTest.png")

while True:
    window.fill((200,200,200))
    b.draw()
    for event in pygame.event.get():
        b.update(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    pygame.display.update()

