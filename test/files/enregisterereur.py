import sqlite3


class Record:
    def __init__(self,name):
        self.__name = name
        self.__idCurrentUser = None
        self.createTable()

    def createTable(self):
        try:
            connection = sqlite3.connect(self.__name)
            cursor = connection.cursor()
            cursor.execute("""
            CREATE TABLE users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom VARCHAR(100),
                prenom VARCHAR(100),
                age INT)
            """)
            connection.commit()
        except:
            print(f"[ERREUR] table exitant")
            connection.rollback()
        finally:
            connection.close()
    
    def addUser(self,nom,prenom,age):
        assert isinstance(nom,str),"le nom n'est pas un string"
        assert isinstance(prenom,str),"le prenom n'est pas un string"
        assert isinstance(age,int),"l'age n'est pas un string"
        try:
            connection = sqlite3.connect(self.__name)
            cursor = connection.cursor()
            user = (nom,prenom,age)
            cursor.execute("INSERT INTO users(nom,prenom,age) VALUES(?,?,?)",user)
            connection.commit()
        except:
            print(f"[ERREUR] addUser")
            connection.rollback()
        finally:
            connection.close()
    
    def delUser(self,id):
        try:
            connection = sqlite3.connect(self.__name)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?",(id,))
            connection.commit()
        except:
            print(f"[ERREUR] delUser")
            connection.rollback()
        finally:
            connection.close()

    def updateUser(self,key,value):
        try:
            connection = sqlite3.connect(self.__name)
            cursor = connection.cursor()
            user = (value,self.__idCurrentUser,)
            if self.__idCurrentUser != None:
                cursor.execute(f"UPDATE users SET {key} = ? WHERE id = ? ",user)
                connection.commit()
        except:
            print(f"[ERREUR] UpdateUser")
            connection.rollback()
        finally:
            connection.close()

    def getUser(self,id):
        try:
            connection = sqlite3.connect(self.__name)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM users WHERE id = ? ",id)
            connection.commit()
            user = cursor.fetchone()
            self.__idCurrentUser = user[0]
            print(f"\nid = {user[0]}, nom = {user[1]}, prenom = {user[2]}, age = {user[3]}\n")
        except:
            print(f"[ERREUR] getUser")
            connection.rollback()
        finally:
            connection.close()

    def printUsers(self):
        users = []
        try:
            connection = sqlite3.connect(self.__name)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM users")
            connection.commit()
            users = cursor.fetchall()
            print("ID       NOM     PRENOM     AGE\n")
            for user in users:
                for element in user:
                    print(element,end="  ")
                print()
        except:
            print(f"[ERREUR] printUser")
            connection.rollback()
        finally:
            connection.close()

    def run(self):
        while True:
            print("\n(1) afficher la liste")
            print("\n(2) ajouter un user")
            print("\n(3) suprimer un user")
            print("\n(4) update un user")
            print("\n(5) get un user")
            print("\n(0) QUIT\n\n")
            choice = int(input("Votre choix : "))
            if choice == 0: break
            if choice == 1: self.printUsers()
            if choice == 2: self.addUser(input("NOM :"),
                             input("PRENOM :"),
                             int(input("AGE :")))
            if choice == 3: self.delUser(int(input("ID :")))
            if choice == 4: self.updateUser(input("KEY :"),input("VALUE :"))
            if choice == 5: self.getUser(input("ID :"))

Record("test.db").run()