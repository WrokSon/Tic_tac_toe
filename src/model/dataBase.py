import sys, os, sqlite3
sys.path.append(os.getcwd())

class DateBase:
    def __init__(self):
        self.__name = "src/resources/database/data.db"
        self.__tablecreate = False
        self.createTables()
        self.initTables
        
    def createTables(self):
        self.createTableUsers()
        self.createTableSettings()

    def createTableUsers(self):
        try:
            connection = sqlite3.connect(self.__name)
            cursor = connection.cursor()
            cursor.execute("""
            CREATE TABLE users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100),
                points INT,
                gameplayed INT,
                image text)
            """)
            connection.commit()
            self.__tablecreate = True
        except:
            print(f"[ERREUR] table users exitant")
            connection.rollback()
            self.__tableExist = True
        finally:
            connection.close()

    def createTableSettings(self):
        try:
            connection = sqlite3.connect(self.__name)
            cursor = connection.cursor()
            cursor.execute("""
            CREATE TABLE settings(
                bg TEXT,
                musicon INT,
                volume INT,
                music TEXT,
                musichuman TEXT,
                musicsolo TEXT,
                musiconline TEXT)
            """)
            connection.commit()
        except:
            print(f"[ERREUR] table settings exitant")
            connection.rollback()
           
        finally:
            connection.close()

    def initTables(self):
        self.initTableUsers()
        self.initTableSettings()

    def initTableUsers(self):
        if not self.__tablecreate: 
            return
        new_users = [(0,"BOT",0,0,"src/resources/images/profile/profilePlayerDefault.png"),
                (1,"Joueur 1",0,0,"src/resources/images/profile/profilePlayerDefault.png"),
                (2,"Joueur 2",0,0,"src/resources/images/profile/profilePlayerDefault.png")
                ]
        try:
            connection = sqlite3.connect(self.__name)
            cursor = connection.cursor()
            for user in new_users : cursor.execute("INSERT INTO users VALUES(?,?,?,?,?)", user) 
            connection.commit()
        except:
            print(f"[ERREUR] user exitant")
            connection.rollback()
        finally:
            connection.close()
    
    def initTableSettings(self):
        #pour musicon 1 = vrai et 0 faux
        if not self.__tablecreate: 
            return
        try:
            connection = sqlite3.connect(self.__name)
            cursor = connection.cursor()
            value = ("src/resources/images/app/background.jpg",1,10,
                     "src/resources/musics/hitting-hard-cinematic-rock-trailer-142396.mp3",
                     "src/resources/musics/drum-percussion-beat-118810.mp3",
                     "src/resources/musics/motivation-hip-hop-epic-sport-hip-hop-background-music-124924.mp3",
                     "src/resources/musics/trap-beat-99191.mp3"
                     )
            cursor.execute("INSERT INTO users VALUES(?,?,?,?,?)", value) 
            connection.commit()
        except:
            print(f"[ERREUR] user exitant")
            connection.rollback()
        finally:
            connection.close()
        
    #methods 
    def executeQueryWithResponse(self,query,args):
        try:
            connection = sqlite3.connect(self.__name)
            cursor = connection.cursor()
            cursor.execute(query,args)
            return cursor.fetchone()
        except:
            print(f"[ERREUR] query with response")
            connection.rollback()
        finally:
            connection.close()
    
    def executeQueryWithoutResponse(self,query,args):
        try:
            connection = sqlite3.connect(self.__name)
            cursor = connection.cursor()
            cursor.execute(query,args)
            connection.commit()
        except:
            print(f"[ERREUR] query without response")
            connection.rollback()
        finally:
            connection.close()

