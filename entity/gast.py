class gast():
    def __init__(self, vorname, nachname):
        self.__vorname = vorname
        self.__nachname = nachname
        self.__reserv = []

    def __str__(self):
        return "{} {} {}".format(self.__vorname, self.__nachname, len(self.__reserv))

    def __repr__(self):
        return "{} {} {}".format(self.__vorname, self.__nachname, len(self.__reserv))

    def __eq__(self, other):
        return self.__vorname == other.__vorname and self.__nachname == other.__nachname

    @property
    def vorname(self):
        return self.__vorname

    @vorname.setter
    def vorname(self, vorname):
        self.__vorname = vorname

    @property
    def nachname(self):
        return self.__nachname

    @nachname.setter
    def nachname(self, nachname):
        self.__nachname = nachname

    @property
    def reserv(self):
        return self.__reserv

    @reserv.setter
    def reserv(self, reserv):
        self.__reserv = reserv
