class reservierung():
    def __init__(self, zimmer, anfang, ende):
        self.__zimmer= zimmer
        if ende<anfang:
            raise AssertionError("invalid dates")
        self.__anfang= anfang
        self.__ende= ende

    def __str__(self):
        return f'Room {self.__zimmer} from {self.__anfang} to {self.__ende}'

    def __repr__(self):
        return f'Room {self.__zimmer} from {self.__anfang} to {self.__ende}'

    @property
    def zimmer(self):
        return self.__zimmer

    @zimmer.setter
    def zimmer(self, zimmer):
        self.__zimmer = zimmer

    @property
    def anfang(self):
        return self.__anfang

    @anfang.setter
    def anfang(self, anfang):
        self.__anfang = anfang

    @property
    def ende(self):
        return self.__ende

    @ende.setter
    def ende(self, ende):
        self.__ende = ende


