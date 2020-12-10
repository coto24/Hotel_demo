def count(d):
    aux = d.jahr
    if (d.monat <= 2):
        aux -= 1
    return int(aux / 4) - int(aux / 100) + int(aux / 400)

class data():
    Monat= [31,28,31,30,31,30,31,31,30,31,30,31]
    def __init__(self, tag, monat, jahr):
        self.__tag= tag
        self.__monat= monat
        self.__jahr= jahr

    def __str__(self):
        return "{}/{}/{}".format(self.__tag, self.__monat, self.__jahr)

    def __repr__(self):
        return "{}/{}/{}".format(self.__tag, self.__monat, self.__jahr)

    def __eq__(self, other):
        return self.__tag==other.__tag and self.__monat==other.__monat and self.__jahr==other.__jahr

    def __lt__(self, other): # < returneaza 1 daca e mai mic strict
        if self.__jahr<other.__jahr:
            return 1
        if self.__jahr>other.__jahr:
            return 0
        if self.__monat<other.__monat:
            return 1
        if self.__monat>other.__monat:
            return 0
        if self.__tag<other.__tag:
            return 1
        if self.__tag>other.__tag:
            return 0
        return 0


    def __sub__(self, other):
        n1 = self.__jahr * 365 + self.__tag
        for i in range(0, self.__monat - 1):
            n1 += data.Monat[i]
        n1 += count(self)
        n2 = other.__jahr * 365 + other.__tag
        for i in range(0, other.__monat - 1):
            n2 += data.Monat[i]
        n2 += count(other)
        return (n1 - n2)

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, tag):
        self.__tag = tag

    @property
    def monat(self):
        return self.__monat

    @monat.setter
    def monat(self, monat):
        self.__monat = monat

    @property
    def jahr(self):
        return self.__jahr

    @jahr.setter
    def jahr(self, jahr):
        self.__jahr = jahr