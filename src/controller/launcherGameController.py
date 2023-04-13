import pygame, sys, os
sys.path.append(os.getcwd())
from pygame.locals import *
from controller.controller import Controller
from model.enums.page import Page
from model.enums.modeGame import ModeGame
from view.launcherGameHumanView import LauncherGameHumanView
from view.launcherGameOnLineView import LauncherGameOnLineView
from view.launcherGameSoloView import LauncherGameSoloView

pygame.init()

class LauncherGameController(Controller):
    def __init__(self,shared):
        self.__shared = shared
        self.__viewHumain = LauncherGameHumanView(self.__shared)
        self.__viewSolo = LauncherGameSoloView(self.__shared)
        self.__viewOnLine = LauncherGameOnLineView(self.__shared)

        if self.__shared["mode"] == ModeGame.HUMAN: self.__view = self.__viewHumain
        if self.__shared["mode"] == ModeGame.BOT: 
            self.__view = self.__viewSolo
        if self.__shared["mode"] == ModeGame.ONLINE: self.__view = self.__viewOnLine
    
    def action(self,event):
        if event.type == pygame.QUIT:
            sys.exit(0)

        if  self.__shared["mode"] == ModeGame.BOT : self.actionSolo()

        if self.__view.getValueBtnHome() or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            self.__shared["page"] = Page.HOME
            self.__view.setValueBtnHome()
            return Page.NEXT
        
        if self.__view.getValueBtnStart():
            if self.__shared["mode"] == ModeGame.HUMAN: self.__shared["page"] = Page.GAME
            if self.__shared["mode"] == ModeGame.BOT:
                namePlayer1 = self.__view.getValueTIBPlayer1() 
                if self.__shared["difficulty"] == "Facile":
                    self.__shared["difficulty"] = "Difficle"
                else:
                    self.__shared["difficulty"] = "Facile"
                if namePlayer1 != "" : self.__shared["NamePlayer1"] = namePlayer1
                self.__shared["page"] = Page.GAMESOLO
            if self.__shared["mode"] == ModeGame.ONLINE: self.__shared["page"] = Page.GAMEONLINE
            self.actionHman()
            self.__view.setValueBtnStart()
            return Page.NEXT
        
        if self.__shared["mode"] == ModeGame.ONLINE : 
            self.actionOnLine()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER : self.__view.setValueIsConnected()

    def actionHman(self):
        if self.__shared["mode"] == ModeGame.HUMAN:
            namePlayer1 = self.__view.getValueTIBPlayer1()
            namePlayer2 = self.__view.getValueTIBPlayer2()
            if namePlayer1 != "" : self.__shared["NamePlayer1"] = namePlayer1
            if namePlayer2 != "" : self.__shared["NamePlayer2"] = namePlayer2
            self.__view.setValueBtnStart()
            self.__view.setValueTIBPlayer1()
            self.__view.setValueTIBPlayer2()
    
    def actionSolo(self):
        if self.__view.getValueBtnDificulty():
            if self.__view.getTextBtnDificulty() == "Facile":
                self.__view.setTextBtnDificulty("Difficle")
            else:
                self.__view.setTextBtnDificulty("Facile")
            self.__view.setValueBtnDificulty()
    
    def actionOnLine(self):
        self.actionOnLineBtnTypConnection()
        self.actionOnLineBtnMassagePlayer()

        if self.__view.getValueBtnConnect():
            self.__shared["IpAddrServer"] = self.__view.getValueTIBIPPlayer2()
            #faire la connexion
            #self.__shared["isConnected"] = True #a modifer par la valeur de retour du serveur
            self.__view.refreshView(self.__shared)
            self.__view.setValueBtnConnect()

    def actionOnLineBtnTypConnection(self):
        if self.__view.getValueBtnTypOfConnection():
            if self.__view.getTextBtnTypOfConnection() == self.__shared["typConnection"][0]:
                self.__view.setTextBtnTypOfConnection(self.__shared["typConnection"][1])
                self.__shared["server"] = True
            else:
                self.__view.setTextBtnTypOfConnection(self.__shared["typConnection"][0])
                self.__shared["server"] = False
            
            self.__view.setValueBtnTypOfConnection()
            self.__view.setValueViewJoin()
            self.__view.refreshView(self.__shared)

    def actionOnLineBtnMassagePlayer(self):
        if self.__view.getValueBtnMessagePlayer():
            msg = self.__view.getValueTIBMessagePlayer()
            if msg != "":
                #envoyer un requette
                if self.__shared["server"] : 
                    self.__shared["msgPlayers"][1] = msg
                else:
                    self.__shared["msgPlayers"][0] = msg           
            self.__view.setValueBtnMessagePlayer()
            self.__view.setValueTIBMessagePlayer()
            self.__view.refreshView(self.__shared)

    def update(self,sharedUpdate):
        #pour mettre a jour le des infos partagés
        self.__shared = sharedUpdate
        if self.__shared["mode"] == ModeGame.HUMAN: self.__view = self.__viewHumain
        if self.__shared["mode"] == ModeGame.BOT: self.__view = self.__viewSolo
        if self.__shared["mode"] == ModeGame.ONLINE: self.__view = self.__viewOnLine
        self.__view.refreshView(self.__shared)

    def run(self):
        while True:
            self.__view.drawAll()
            for event in pygame.event.get():
                if self.action(event) == Page.NEXT:
                    return self.__shared
                self.__view.update(event)
                