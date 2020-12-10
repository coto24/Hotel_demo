from entity.gast import gast
from entity.zimmer import zimmer
from entity.reservierung import reservierung
from entity.data import data
import pickle

class repo:
    def __init__(self):
        self.__listg = []
        self.__listz = []

    def storeToFile(self):
        with open("data/gast.txt", "wb") as f:
            pickle.dump(self.__listg,f)
        f.close()
        with open("data/zimmer.txt", "wb") as f:
            pickle.dump(self.__listz,f)
        f.close()


    def loadFromFile(self):
        with open("data/gast.txt","rb") as f:
            self.__listg = pickle.load(f)
        f.close()
        with open("data/zimmer.txt","rb") as f:
            self.__listz = pickle.load(f)
        f.close()

    def print_guest(self):
        for i in self.listg:
            print(i)

    @property
    def listg(self):
        return self.__listg

    @listg.setter
    def listg(self, aux):
        self.__listg = aux
    @property
    def listz(self):
        return self.__listz

    @listz.setter
    def listz(self, aux):
        self.__listz = aux