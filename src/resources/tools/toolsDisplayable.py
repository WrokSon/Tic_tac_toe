import pygame, string
from pygame.locals import *
from tkinter import Tk,filedialog


class TextInputBox:
    def __init__(self, window, position=(0, 0), dimension=(300, 50), maximum=10):
        self.position = position
        self.__dimension = dimension
        self.__window = window
        self.__text = ""
        self.__active = False
        self.__maxC = maximum
        self.__alphabet = string.ascii_letters + string.digits + string.punctuation + " "
        self.__length = 0
        self.__animationTime = pygame.time.get_ticks()
        self.rect = pygame.Rect(self.position, self.__dimension)

    def getLength(self):
        return self.__length

    def draw(self):
        self.drawBG()
        self.drawText()
        self.animation()

    def drawBG(self):
        colorBg = (50, 50, 50)  # black
        colorOutline = (255, 255, 255) if self.__active else (50, 50, 50)  # white or black
        pygame.draw.rect(self.__window, colorBg, self.rect)
        pygame.draw.rect(self.__window, colorOutline, self.rect, 3)

    def drawText(self):
        font = pygame.font.Font(None, 40)
        text = font.render(self.__text, True, "white")
        self.__window.blit(text, text.get_rect(center=self.rect.center))

    def contains(self, pos):
        if self.position[0] <= pos[0] <= self.position[0] + self.__dimension[0]:
            if self.position[1] <= pos[1] <= self.position[1] + self.__dimension[1]:
                return True
        return False

    def animation(self):
        if self.__active:
            time = (pygame.time.get_ticks() - self.__animationTime) // 500
            if (time % 2) == 0 and self.__text == "":
                self.__text += "|"
            if (time % 2) == 1 and self.__text == "|":
                self.__text = self.__text[:-1]
            else:
                if len(self.__text) != self.__length and self.__length >= 1:
                    self.__text = self.__text[1:]
        else:
            if len(self.__text) != self.__length:
                self.__text = self.__text[1:]

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.contains(pygame.mouse.get_pos()):
                self.active()
            else:
                self.notActive()
        if event.type == pygame.KEYDOWN and self.__active:
            if event.key == K_BACKSPACE:
                self.__text = self.__text[:-1]
                self.__length -= 1 if self.__length > 0 else 0
            else:
                c = event.unicode
                if c in self.__alphabet and len(self.__text) < self.__maxC:
                    self.__text += c
                    self.__length += 1
        self.draw()

    def active(self):
        self.__active = not self.__active
    
    def notActive(self):
        self.__active = False

    def getText(self):
        return self.__text

    def setText(self, newText):
        self.__text = str(newText)
        self.__length = len(str(newText))

    def changePos(self, pos):
        self.position = pos
        self.rect = pygame.Rect(self.position, self.__dimension)

#set the button when that active, that makes buggs when you don't do that
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
        self.rect = pygame.Rect(self.position, self.__dimension)

    def getText(self):
        return self.__text

    def setText(self,newText):
        self.__text = newText

    def isActive(self):
        return self.__active

    def notActive(self):
        self.__active = False
        self.__colorText = "black"
        self.__colorBg = self.__colorNormal

    def draw(self):
        self.drawBg()
        self.drawText()

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


class Text:
    def __init__(self, window, text, position, color="black", size=30):
        self.__window = window
        self.__text = text
        self.__size = size
        self.position = position
        self.__color = color
        self.__font = pygame.font.Font(None, self.__size)
        self.draw()

    def getText(self):
        return self.__text

    def setColor(self,newColor):
        self.__color = newColor

    def setFont(self,newFont):
        self.__font = pygame.font.Font(newFont, self.__size)

    def setText(self, newText):
        self.__text = newText

    def draw(self):
        text = self.__font.render(self.__text, True, self.__color)
        self.__window.blit(text, self.position)


class SaveData:
    def __init__(self, path="", name="data"):
        self.__data = []
        self.__path = path
        self.__name = self.__path + name

    def add(self, text):
        with open(self.__name, 'a', encoding="utf-8") as file:
            file.write(f"{str(text)}\n")

    def save(self, newData):
        # newData a matrix
        for i in range(len(newData)):
            line = ""
            for j in range(len(newData[i])):
                line += f"{newData[i][j]} "
            self.add(line)

    def uptade(self):
        try:
            with open(self.__name, 'r', encoding="utf-8") as file:
                text = file.readlines()
                for line in text:
                    self.__data.append(line.split(" ")[:-1])
                for i in range(len(self.__data)):
                    for j in range(len(self.__data[i])):
                        self.__data[i][j] = float(self.__data[i][j])
        except:
            with open(self.__name, 'w', encoding="utf-8") as file:
                pass

    def getData(self):
        self.uptade()
        return self.__data

    def clear(self):
        with open(self.__name, 'w', encoding="utf-8") as file:
            pass

class FileChooser:
    def __init__(self):
        self.__fileSelected = ""

    def getFileSelected(self):
        return self.__fileSelected
    
    def selectFile(self,exentions=[("All files","*.*"),("All files","*.*")]):
        top = Tk()
        top.withdraw()  # hide window
        self.__fileSelected = filedialog.askopenfilename(parent=top, title = "Select file",filetypes = exentions)
        top.destroy()
        return self.__fileSelected
    
    def saveFile(self,exentions=[("All files","*.*"),("All files","*.*")]):
        top = Tk()
        top.withdraw()  # hide window
        self.__fileSelected = filedialog.asksaveasfilename(parent=top, title = "Save file",filetypes = exentions)
        top.destroy()
        return self.__fileSelected
    