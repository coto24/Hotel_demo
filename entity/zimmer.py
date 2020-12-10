class zimmer():
    def __init__(self, nummer, amg, preis, farbe, meerblick):
            self.__nummer = nummer
            self.__amg = amg
            self.__preis = preis
            self.__farbe = farbe
            self.__meerblick = meerblick # 1 sau 0

    def __str__(self):
        return "Room{} can host{} persons, has the price of {} per night, has the color of the walls {} {};".format(self.__nummer, self.__amg,self.__preis,self.__farbe,'has seaview' if self.__meerblick==1 else "doesn't have seaview")
    def __repr__(self):
        return "Room{} can host{} persons, has the price of {} per night, has the color of the walls {} {};".format(self.__nummer, self.__amg,self.__preis,self.__farbe,'has seaview' if self.__meerblick==1 else "doesn't have seaview")
    def __eq__(self, other):
        return self.__nummer==other.__nummer
    @property
    def nummer(self):
        return self.__nummer
    @nummer.setter
    def nummer(self, nummer):
        self.__nummer = nummer
    @property
    def amg(self):
        return self.__amg
    @amg.setter
    def amg(self, amg):
        self.__amg = amg
    @property
    def preis(self):
        return self.__preis
    @preis.setter
    def preis(self, preis):
        self.__preis = preis
    @property
    def farbe(self):
        return self.__farbe
    @farbe.setter
    def farbe(self, farbe):
        self.__farbe = farbe
    @property
    def meerblick(self):
        return self.__meerblick
    @meerblick.setter
    def meerblick(self, meerblick):
        self.__meerblick = meerblick
    @property
    def reserv(self):
        return self.__reserv
    @reserv.setter
    def reserv(self, reserv):
        self.__reserv = reserv
