import sys, os, sqlite3
from dataBase import DataBase
sys.path.append(os.getcwd())

class QueryExecutor:
    def __init__(self):
        self.__dataBase = DataBase()