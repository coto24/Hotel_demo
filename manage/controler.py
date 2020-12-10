from datetime import date
from entity.data import data
from entity.zimmer import zimmer

heute = data(date.today().day, date.today().month, date.today().year)

class controler:
    def __init__(self, repo):
        self.__repo = repo

    @property
    def repo(self):
        return self.__repo

    @repo.setter
    def repo(self, aux):
        self.__repo = aux

    def save(self):
        self.repo.storeToFile()

    def load(self):
        self.repo.loadFromFile()

    def add_guest(self, aux):  # aux e de tip gast
        if not aux in self.repo.listg:
            self.repo.listg.append(aux)

    def update_guest(self, aux, neu):
        for i in range(0, len(self.repo.listg)):
            if self.repo.listg[i] == aux:
                self.repo.listg[i].nachname = neu

    def delete_guest(self, aux):
        for i in range(0, len(self.repo.listg)):
            if self.repo.listg[i] == aux:
                self.repo.listg.pop(i)

    def print_guest(self):
        aux = ''
        for i in self.repo.listg:
            aux += str(i) +'\n'
        return aux

    def add_room(self, aux):  # aux e de tip zimmer
        self.repo.listz.append(aux)

    def change_price(self, nr, preis):
        for i in range(len(self.repo.listz)):
            if self.repo.listz[i].nummer == nr:
                self.repo.listz[i].preis = preis

    def delete_room(self, nr):
        for i in range(0, len(self.repo.listz)):
            if self.repo.listz[i].nummer == nr:
                self.repo.listz.pop(i)

    def print_rooms(self):
        aux = ''
        for i in self.repo.listz:
            aux += str(i) + '\n'
        return aux

    def no_reserv_guest(self):
        for i in self.repo.listg:
            if len(i.reserv) == 0:
                print(i)

    def today_valid(self):
        for i in self.repo.listg:
            for j in i.reserv:
                if j.ende < heute:
                    i.reserv.remove(j)

    def filter_room(self, p, m, c):
        # 1 mai scump de x euro
        # 2 mai ieftin de x euro
        # 3 de x euro
        aux = ''
        for i in self.repo.listz:
            if i.preis > p and c == 1 and m == i.meerblick:
                aux += str(i.nummer) + ' '
            if i.preis < p and c == 2 and m == i.meerblick:
                aux += str(i.nummer) + ' '
            if i.preis == p and c == 3 and m == i.meerblick:
                aux += str(i.nummer) + ' '
        return aux

    def available_today(self):
        aux = []
        for i in self.repo.listz:
            aux.append(i.nummer)
        for i in self.repo.listg:
            for j in i.reserv:
                if j.zimmer in aux and (heute < j.ende or heute == j.ende) and (heute < j.ende or heute == j.ende):
                    aux.remove(j.zimmer)
        return aux

    def cancel(self, aux, nr_ord):  # aux tip gast
        for i in range(len(self.repo.listg)):
            if self.repo.listg[i] == aux:
                self.repo.listg[i].reserv.pop(nr_ord)

    def make_reservation(self, gast, aux):  # aux e de tip reservierung
        if gast not in self.repo.listg:
            self.repo.listg.append(gast)
        self.repo.listg[self.repo.listg.index(gast)].reserv.append(aux)
        preis=0
        for i in self.repo.listz:
            if i.nummer == aux.zimmer:
                preis = i.preis
        print("Sie müssen {} € bezahlen".format((aux.ende - aux.anfang) * preis))
