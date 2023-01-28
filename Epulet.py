class Epulet:
    def __init__(self, sor):
        self.nev = sor[0]
        self.varos = sor[1]
        self.orszag = sor[2]
        self.__magassag = float(sor[3].replace(',', '.'))
        self.emelet = int(sor[4])
        self.epult = int(sor[5])

    def getmagassag(self):
        return self.__magassag

    def __str__(self):
        return f"{self.nev}, {self.varos}, {self.orszag}, {self.__magassag}, {self.emelet}, {self.epult}"
