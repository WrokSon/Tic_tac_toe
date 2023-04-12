import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from resources.tools.toolsDisplayable import Text, Button,TextInputBox, FileChooser

pygame.init()

class SettingsView:
    def __init__(self,shared):
        self.__shared = shared
        self.__windowTitle = "Tic Tac Toe | Parametres"
        self.__window = self.__shared["window"]
        self.createAll()
    
    def getFileSelected(self):
        return self.__fileSlected

    def getShared(self):
        return self.__shared

    def getValueBtnDefault(self):
        return self.__btnDefault.isActive()

    def getValueBtnHome(self):
        return self.__btnHomeGo.isActive()
    
    def getValueBtnChangeBackgound(self):
        return self.__btnChangBg.isActive()
    
    def getValueBtnGame(self):
        return self.__btnGameGo.isActive()

    def getValueBtnSetMusicOn(self):
        return self.__btnSetMusicOn.isActive()
    
    def getValueBtnSetMusic(self):
        return self.__btnSetMusic.isActive()
    
    def getValueBtnSetMusicSolo(self):
        return self.__btnSetMusicSolo.isActive()
    
    def getValueBtnSetMusicHuman(self):
        return self.__btnSetMusicHuman.isActive()
    
    def getValueBtnSetMusicOnLine(self):
        return self.__btnSetMusicOnLine.isActive()

    def getValueBtnSetProfileName1(self):
        return self.__btnSetProfileName1.isActive()

    def getValueBtnSetProfileName2(self):
        return self.__btnSetProfileName2.isActive()
    
    def getValueBtnSetProfileImage1(self):
        return self.__btnSetProfileImage1.isActive()
    
    def getValueBtnSetProfileImage2(self):
        return self.__btnSetProfileImage2.isActive()

    def getValueInputBox(self):
        return self.__tIBChangeValue.getText()

    def setValueInputBox(self):
        self.__tIBChangeValue.setText('')

    def setBackground(self,newBg):
        if newBg != "":
            self.__shared["bg"] = pygame.image.load(newBg)
            self.createBg()

    def setValueBtnChangeBackgound(self):
        self.__btnChangBg.notActive()

    def setValueBtnDefault(self):
        self.__btnDefault.notActive()

    def setValueBtnHome(self):
        self.__btnHomeGo.notActive()

    def setValueBtnGame(self):
        self.__btnGameGo.notActive()

    def setValueBtnSetMusicOn(self):
        self.__btnSetMusicOn.notActive()
    
    def setValueBtnSetMusic(self):
        self.__btnSetMusic.notActive()
    
    def setValueBtnSetMusicSolo(self):
        self.__btnSetMusicSolo.notActive()
    
    def setValueBtnSetMusicHuman(self):
        self.__btnSetMusicHuman.notActive()
    
    def setValueBtnSetMusicOnLine(self):
        self.__btnSetMusicOnLine.notActive()

    def setBtnTextMusicOn(self,newValue):
        self.__btnSetMusicOn.setText(newValue)

    def setValueBtnSetProfileName1(self):
        self.__btnSetProfileName1.notActive()

    def setValueBtnSetProfileName2(self):
        self.__btnSetProfileName2.notActive()
    
    def setValueBtnSetProfileImage1(self):
        self.__btnSetProfileImage1.notActive()
    
    def setValueBtnSetProfileImage2(self):
        self.__btnSetProfileImage2.notActive()

    def createAll(self):
        self.createFileChooser()
        self.createBg()
        self.createButtons()
        self.createTexts()
        self.createTextInputBox()
        pygame.display.update()
    
    def createButtons(self):
        self.__dimBtns = (45,45)
        self.__BtnPosX = [260,650]
        self.__btnDefault = Button(self.__window,"D",position=(660,350),dimension=self.__dimBtns)
        self.__btnHomeGo = Button(self.__window,"-",position=(10,10),dimension=self.__dimBtns)
        self.__btnGameGo = Button(self.__window,"+",position=(10,340),dimension=self.__dimBtns)
        self.__btnChangBg = Button(self.__window,"F",position=(self.__BtnPosX[0],62),dimension=self.__dimBtns)
        self.createButtonsMusic()
        self.createButtonsProfile()

    def drawAll(self):
        self.__window.blit(self.__imgBg,(0,0))
        pygame.display.set_caption(self.__windowTitle)
        self.drawButtons()
        self.drawTexts()
        self.drawTextInputBox()
        pygame.display.update()

    def drawButtons(self):
        self.__btnHomeGo.draw()
        self.__btnGameGo.draw()
        self.__btnChangBg.draw()
        self.__btnDefault.draw()
        self.drawButtonsMusic()
        self.drawButtonsProfile()

    def update(self,event):
        self.updateButtons(event)
        self.updateTextInputBox(event)
        self.doEvent(event)

    def doEvent(self,event):
        if self.__btnChangBg.isActive():
            self.__fileSlected = self.__fileChooser.selectFile(self.__extensionsImgs)
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if self.__colorText == ["red","black"]:
                self.__colorText = ["blue","white"]
            else:
                self.__colorText = ["red","black"]

        self.doEventBtnsMusic()
        self.doEventBtnProfile()

    def doEventBtnsMusic(self):  
        if self.__btnSetMusic.isActive() or self.__btnSetMusicHuman.isActive() or self.__btnSetMusicSolo.isActive() or self.__btnSetMusicOnLine.isActive():
            self.__fileSlected = self.__fileChooser.selectFile(self.__extensionsMusics)

    def doEventBtnProfile(self):
        if self.__btnSetProfileImage1.isActive() or self.__btnSetProfileImage2.isActive():
            self.__fileSlected = self.__fileChooser.selectFile(self.__extensionsImgs)

    def updateButtons(self, event):
        self.__btnHomeGo.update(event)
        self.__btnGameGo.update(event)
        self.__btnChangBg.update(event)
        self.__btnDefault.update(event)
        self.updateButtonsMusic(event)
        self.updateButtonsProfile(event)

    def createBg(self):
        bgImg = pygame.image.load(self.__shared["bg"])
        self.__imgBg = pygame.transform.scale(bgImg, pygame.display.get_surface().get_size())

    def createFileChooser(self):
        self.__extensionsImgs = [("PNG","*.png"),("JPG","*.jpg")]
        self.__extensionsMusics = [("MP3","*.mp3"),("WAV","*.wav"),("OGG","*.ogg")]
        self.__fileChooser = FileChooser()

    def refreshView(self,newShared):
        self.__shared = newShared
        self.createBg()

    def createTexts(self):
        self.__colorText = ["blue","white"]
        self.__tPosX = [30,430]
        self.__fontText = self.__shared["fonts"][1]
        self.__sizeText = 15
        self.__tTitle = Text(self.__window,"Parametres",(170,10),self.__colorText[1],50)
        self.__tChangBg = Text(self.__window,"Changer le fond d'ecran",(self.__tPosX[0],75),self.__colorText[1],self.__sizeText)
        self.__tTitle.setFont(self.__shared["fonts"][3])
        self.__tChangBg.setFont(self.__fontText)
        self.createTextsMusic()
        self.createTextsProfile()

    def drawTexts(self):
        self.__tTitle.draw()
        self.__tChangBg.draw()
        self.drawTextMusic()
        self.drawTextProfile()
        self.__tTitle.setColor(self.__colorText[0])
        self.__tChangBg.setColor(self.__colorText[1])

    def createTextInputBox(self):
        self.__fileSlected = ""
        self.__tIBChangeValue = TextInputBox(self.__window,(215,340))

    def drawTextInputBox(self):
        self.__tIBChangeValue.draw()

    def updateTextInputBox(self,event):
        self.__tIBChangeValue.update(event)

    def createButtonsMusic(self):
        btnMusicPosY = [i*47 +105 for i in range(5)]
        self.__btnSetMusicOn = Button(self.__window,"ACTIVER",position=(self.__BtnPosX[0]-30,btnMusicPosY[0]+5),dimension=(100,40),sizeText=20)
        self.__btnSetMusic = Button(self.__window,"G",dimension=self.__dimBtns,position=(self.__BtnPosX[0],btnMusicPosY[1]))
        self.__btnSetMusicSolo = Button(self.__window,"S",dimension=self.__dimBtns,position=(self.__BtnPosX[0],btnMusicPosY[2]))
        self.__btnSetMusicHuman = Button(self.__window,"D",dimension=self.__dimBtns,position=(self.__BtnPosX[0],btnMusicPosY[3]))
        self.__btnSetMusicOnLine = Button(self.__window,"E",dimension=self.__dimBtns,position=(self.__BtnPosX[0],btnMusicPosY[4]))

    def drawButtonsMusic(self):
        self.__btnSetMusicOn.draw()
        self.__btnSetMusic.draw()
        self.__btnSetMusicSolo.draw()
        self.__btnSetMusicHuman.draw()
        self.__btnSetMusicOnLine.draw()
   
    def updateButtonsMusic(self,event):
        self.__btnSetMusicOn.update(event)
        self.__btnSetMusic.update(event)
        self.__btnSetMusicSolo.update(event)
        self.__btnSetMusicHuman.update(event)
        self.__btnSetMusicOnLine.update(event)

    def createTextsMusic(self):
        tMusicPosY = [i*47 +125 for i in range(5)]
        self.__tSetMusicOn = Text(self.__window,"Musique",(self.__tPosX[0],tMusicPosY[0]),self.__colorText[1],self.__sizeText)
        self.__tSetMusic = Text(self.__window,"Changer la musique general",(self.__tPosX[0],tMusicPosY[1]),self.__colorText[1],self.__sizeText)
        self.__tSetMusicSolo = Text(self.__window,"Changer la musique Solo",(self.__tPosX[0],tMusicPosY[2]),self.__colorText[1],self.__sizeText)
        self.__tSetMusicHuman = Text(self.__window,"Changer la musique 1V1",(self.__tPosX[0],tMusicPosY[3]),self.__colorText[1],self.__sizeText)
        self.__tSetMusicOnLine = Text(self.__window,"Changer la musique en ligne",(self.__tPosX[0],tMusicPosY[4]),self.__colorText[1],self.__sizeText)

        self.__tSetMusicOn.setFont(self.__fontText)
        self.__tSetMusic.setFont(self.__fontText)
        self.__tSetMusicSolo.setFont(self.__fontText)
        self.__tSetMusicHuman.setFont(self.__fontText)
        self.__tSetMusicOnLine.setFont(self.__fontText)

    def drawTextMusic(self):
        self.__tSetMusicOn.draw()
        self.__tSetMusic.draw()
        self.__tSetMusicSolo.draw()
        self.__tSetMusicHuman.draw()
        self.__tSetMusicOnLine.draw()

        self.__tSetMusicOn.setColor(self.__colorText[1])
        self.__tSetMusic.setColor(self.__colorText[1])
        self.__tSetMusicSolo.setColor(self.__colorText[1])
        self.__tSetMusicHuman.setColor(self.__colorText[1])
        self.__tSetMusicOnLine.setColor(self.__colorText[1])

    def createButtonsProfile(self):
        btnProfilePosY = [i*50 +100 for i in range(5)]
        self.__btnSetProfileName1 = Button(self.__window,"N1",position=(self.__BtnPosX[1],btnProfilePosY[0]),dimension=self.__dimBtns)
        self.__btnSetProfileName2 = Button(self.__window,"N2",position=(self.__BtnPosX[1],btnProfilePosY[1]),dimension=self.__dimBtns)
        self.__btnSetProfileImage1 = Button(self.__window,"P1",position=(self.__BtnPosX[1],btnProfilePosY[2]),dimension=self.__dimBtns)
        self.__btnSetProfileImage2 = Button(self.__window,"P2",position=(self.__BtnPosX[1],btnProfilePosY[3]),dimension=self.__dimBtns)
    
    def drawButtonsProfile(self):
        self.__btnSetProfileName1.draw()
        self.__btnSetProfileName2.draw()
        self.__btnSetProfileImage1.draw()
        self.__btnSetProfileImage2.draw()
    
    def updateButtonsProfile(self,event):
        self.__btnSetProfileName1.update(event)
        self.__btnSetProfileName2.update(event)
        self.__btnSetProfileImage1.update(event)
        self.__btnSetProfileImage2.update(event)

    def createTextsProfile(self):
        tProfilePosY = [i*50 +115 for i in range(4)]
        self.__tSetProfileName1 = Text(self.__window,"Changer le nom du joueur 1",(self.__tPosX[1],tProfilePosY[0]),self.__colorText[1],self.__sizeText)
        self.__tSetProfileName2 = Text(self.__window,"Changer le nom du joueur 2",(self.__tPosX[1],tProfilePosY[1]),self.__colorText[1],self.__sizeText)
        self.__tSetProfileImage1 = Text(self.__window,"Changer l'image du joueur 1",(self.__tPosX[1],tProfilePosY[2]),self.__colorText[1],self.__sizeText)
        self.__tSetProfileImage2 = Text(self.__window,"Changer l'image du joueur 2",(self.__tPosX[1],tProfilePosY[3]),self.__colorText[1],self.__sizeText)

        self.__tSetProfileName1.setFont(self.__fontText)
        self.__tSetProfileName2.setFont(self.__fontText)
        self.__tSetProfileImage1.setFont(self.__fontText)
        self.__tSetProfileImage2.setFont(self.__fontText)

    def drawTextProfile(self):
        self.__tSetProfileName1.draw()
        self.__tSetProfileName2.draw()
        self.__tSetProfileImage1.draw()
        self.__tSetProfileImage2.draw()

        self.__tSetProfileName1.setColor(self.__colorText[1])
        self.__tSetProfileName2.setColor(self.__colorText[1])
        self.__tSetProfileImage1.setColor(self.__colorText[1])
        self.__tSetProfileImage2.setColor(self.__colorText[1])

