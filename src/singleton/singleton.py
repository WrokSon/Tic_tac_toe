import pygame, sys, os, socket
from pygame.locals import *
pygame.init()
sys.path.append(os.getcwd())
from model.enums.modeGame import ModeGame
from model.enums.page import Page

class Shared:
    def loadFonts():
        fonts = []
        fonts.append("src/resources/fonts/full_pack_2025/full Pack 2025.ttf")
        fonts.append("src/resources/fonts/freshman/Freshman.ttf")
        fonts.append("src/resources/fonts/karmatic_arcade/ka1.ttf")
        fonts.append("src/resources/fonts/super_mario_256/SuperMario256.ttf")
        return fonts

    #variables partagés
    dimWindow = (720,400)
    window = pygame.display.set_mode(dimWindow)
    bg = "src/resources/images/app/background.jpg"
    mode = ModeGame.NOMODE
    page = Page.PRESENTATION
    fonts = loadFonts()
    namePlayer1 = "Joueur 1"
    namePlayer2 = "Joueur 2"
    namePlayerOneLine = "Joueur 2"
    nameBot = "Bot "
    imageBot = "src/resources/images/profile/profilePlayerDefault.png"
    imagePlayer1 = "src/resources/images/profile/profilePlayerDefault.png"
    imagePlayer2 = "src/resources/images/profile/profilePlayerDefault.png"
    imagePlayerOnLine = "src/resources/images/profile/profilePlayerDefault.png"
    victoriesPlayer1 = 0
    victoriesPlayer2 = 0
    currentMusic = ""
    music1V1 = "src/resources/musics/drum-percussion-beat-118810.mp3"
    musicGeneral = "src/resources/musics/hitting-hard-cinematic-rock-trailer-142396.mp3"
    musicSolo = "src/resources/musics/motivation-hip-hop-epic-sport-hip-hop-background-music-124924.mp3"
    musicOnLine = "src/resources/musics/trap-beat-99191.mp3"
    musicOn = True
    musicVolume = 0.1
    difficulty = "Facile"
    difficultyList = ["Facile","Difficle"]
    server = False
    isConnected = False
    myIpAddr = socket.gethostbyname(socket.gethostname())
    iPAddrServer = myIpAddr
    iPAddrClient = myIpAddr
    port = 7639
    msgPlayers = ["Bienvenu(e)","Bienvenu(e)"]
    typConnection = ["INVITE","HOTE"]

    #mets tous par defaut
    def default():
        Shared.bg = "src/resources/images/app/background.jpg"
        Shared.page = Page.SETTINGS
        Shared.fonts = Shared.loadFonts()
        Shared.namePlayer1 = "Joueur 1"
        Shared.namePlayer2 = "Joueur 2"
        Shared.imagePlayer1 = "src/resources/images/profile/profilePlayerDefault.png"
        Shared.imagePlayer2 = "src/resources/images/profile/profilePlayerDefault.png"
        Shared.victoriesPlayer1 = 0
        Shared.victoriesPlayer2 = 0
        Shared.currentMusic = ""
        Shared.music1V1 = "src/resources/musics/drum-percussion-beat-118810.mp3"
        Shared.musicGeneral = "src/resources/musics/hitting-hard-cinematic-rock-trailer-142396.mp3"
        Shared.musicSolo = "src/resources/musics/motivation-hip-hop-epic-sport-hip-hop-background-music-124924.mp3"
        Shared.musicOnLine = "src/resources/musics/trap-beat-99191.mp3"
        Shared.musicOn = True
        Shared.musicVolume = 0.1
        Shared.difficulty = "Facile"
        Shared.server = False
        Shared.isConnected = False
        Shared.msgPlayers = ["Bienvenu(e)","Bienvenu(e)"]
        Shared.iPAddrServer = Shared.iPAddrClient
    
    #renvoie une liste avec les cles et son dictionnaire pour sauver en local
    def saveInfo():
        listKeys = ["bg","NamePlayer1","NamePlayer2","ImagePlayer1","ImagePlayer2",
                    "Music1V1","MusicGeneral","MusicSolo","MusicOnLine","MusicOn",
                    "MusicVolume","victoriesPlayer1","victoriesPlayer2","iPAddrServer"]
        shared = {}
        shared["bg"] = Shared.bg
        shared["NamePlayer1"] = Shared.namePlayer1
        shared["NamePlayer2"] = Shared.namePlayer2
        shared["ImagePlayer1"] = Shared.imagePlayer1
        shared["ImagePlayer2"] = Shared.imagePlayer2
        shared["victoriesPlayer1"] = Shared.victoriesPlayer1
        shared["victoriesPlayer2"] = Shared.victoriesPlayer2
        shared["Music1V1"] = Shared.music1V1
        shared["MusicGeneral"] = Shared.musicGeneral
        shared["MusicSolo"] = Shared.musicSolo
        shared["MusicOnLine"] = Shared.musicOnLine
        shared["MusicOn"] = "1" if Shared.musicOn else "0"
        shared["MusicVolume"] = Shared.musicVolume
        shared["iPAddrServer"] = Shared.iPAddrServer
        return (listKeys,shared)
    
    #remets les valeur avec les bons valeurs 
    def getInfo(shared):
        Shared.bg = shared["bg"]
        Shared.namePlayer1 = shared["NamePlayer1"]
        Shared.namePlayer2 = shared["NamePlayer2"]
        Shared.imagePlayer1 = shared["ImagePlayer1"] 
        Shared.imagePlayer2 = shared["ImagePlayer2"]
        Shared.victoriesPlayer1 = shared["victoriesPlayer1"]
        Shared.victoriesPlayer2 = shared["victoriesPlayer2"]
        Shared.music1V1 = shared["Music1V1"]
        Shared.musicGeneral = shared["MusicGeneral"]
        Shared.musicSolo = shared["MusicSolo"]
        Shared.musicOnLine = shared["MusicOnLine"]
        Shared.musicOn = True if shared["MusicOn"] == "1" else False
        Shared.musicVolume = shared["MusicVolume"] 
        Shared.iPAddrServer = shared["iPAddrServer"]

