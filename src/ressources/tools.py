import pygame
import string
from pygame.locals import *


class TextInputBox:
    def __init__(self, window, position=(0, 0), dimension=(300, 50), maximum=10):
        self.position = position
        self.__dimension = dimension
        self.__window = window
        self.__text = ""
        self.__active = False
        self.__maxC = maximum
        self.__alphabet = string.ascii_letters + string.digits + string.punctuation + " "
        self.__length = len(self.__text)
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

    def getText(self):
        return self.__text

    def setText(self, newText):
        self.__text = str(newText)
        self.__length = len(str(newText))

    def changePos(self, pos):
        self.position = pos
        self.rect = pygame.Rect(self.position, self.__dimension)


class Button:
    def __init__(self, window, text="Button", hoverColor=(200, 190, 250), color=(220, 220, 220), position=(0, 0),
                 dimension=(140, 50)):
        self.position = position
        self.__dimension = dimension
        self.__window = window
        self.__text = text
        self.__active = False
        self.__hoverColorBg = hoverColor
        self.__colorBg = color
        self.__colorNormal = color
        self.__colorText = "black"
        self.rect = pygame.Rect(self.position, self.__dimension)

    def isActive(self):
        return self.__active

    def draw(self):
        self.drawBg()
        self.drawText()

    def drawText(self):
        font = pygame.font.Font(None, 40)
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
            self.__active = False
            self.__colorText = "black"
            self.__colorBg = self.__colorNormal
        self.draw()

    def changePos(self, pos):
        self.position = pos
        self.rect = pygame.Rect(self.position, self.__dimension)


class Text:
    def __init__(self, window, text, position, color="black", size=30):
        self.__window = window
        self.__text = text
        self.position = position
        self.__color = color
        self.font = pygame.font.Font(None, size)
        self.draw()

    def getText(self):
        return self.__text

    def setText(self, newText):
        self.__text = newText

    def draw(self):
        text = self.font.render(self.__text, True, self.__color)
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


class DropDown:
    # taken from :
    # https://stackoverflow.com/questions/59236523/trying-creating-dropdown-menu-pygame-but-got-stuck/65369938#65369938
    def __init__(self, window, options, color_menu, color_option, position, dimension, text="DropDown"):
        self.window = window
        self.color_menu = color_menu
        self.color_option = color_option
        self.position = position
        self.dimension = dimension
        self.rect = pygame.Rect(position, dimension)
        self.font = pygame.font.Font(None, 40)
        self.main = text
        self.options = options
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    def draw(self):
        pygame.draw.rect(self.window, self.color_menu[self.menu_active], self.rect, 0)
        msg = self.font.render(self.main, 1, (255, 255, 255))
        self.window.blit(msg, msg.get_rect(center=self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.options):
                rect = self.rect.copy()
                rect.y += (i + 1) * self.rect.height
                pygame.draw.rect(self.window, self.color_option[1 if i == self.active_option else 0], rect, 0)
                msg = self.font.render(text, 1, (255, 255, 255))
                self.window.blit(msg, msg.get_rect(center=rect.center))

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)

        self.active_option = -1
        for i in range(len(self.options)):
            rect = self.rect.copy()
            rect.y += (i + 1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.draw_menu = False
                    return self.active_option
        return -1

    def setText(self, text):
        self.main = text

    def changePos(self, pos):
        self.position = pos
        self.rect = pygame.Rect(self.position, self.dimension)
