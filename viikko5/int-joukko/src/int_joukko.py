KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        try:
            self.kapasiteetti = kapasiteetti
            self.kasvatuskoko = kasvatuskoko
        except ValueError:
            raise Exception("Kapasiteetin ja kasvatuskoon on oltava int-tyypppiä")
        
        self.taulukko = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0


    def kuuluu(self, luku):
        if luku in self.taulukko:
            return True
        else:
            return False


    def lisaa(self, luku):      
        if self.kuuluu(luku):
            return False
        
        self.taulukko[self.alkioiden_lkm] = luku
        self.alkioiden_lkm += 1

        if self.alkioiden_lkm % len(self.taulukko) == 0:
            apu_taulukko = [0]*self.alkioiden_lkm
            self.kopioi_taulukko(self.taulukko, apu_taulukko)
            self.taulukko = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_taulukko(apu_taulukko, self.taulukko)
        return True


    def poista(self, luku):
        if not self.kuuluu(luku):
            return False

        kohta_loytynyt = False
        for alkio in range(0, self.alkioiden_lkm):
            if luku == self.taulukko[alkio] and not kohta_loytynyt:
                kohta_loytynyt = True
            if kohta_loytynyt:
                self.taulukko[alkio] = self.taulukko[alkio + 1]

        self.taulukko[self.alkioiden_lkm] = 0
        self.alkioiden_lkm = self.alkioiden_lkm - 1
        return True


    def kopioi_taulukko(self, alkup_taul, kopio):
        for alkio in range(0, len(alkup_taul)):
            kopio[alkio] = alkup_taul[alkio]


    def mahtavuus(self):
        return self.alkioiden_lkm


    def int_listaksi(self):
        taulu = [0] * self.alkioiden_lkm

        for alkio in range(0, len(taulu)):
            taulu[alkio] = self.taulukko[alkio]

        return taulu


    @staticmethod
    def yhdiste(a, b):
        yhdiste_joukko = IntJoukko()
        a_taulu = a.int_listaksi()
        b_taulu = b.int_listaksi()

        for i in range(0, len(a_taulu)):
            yhdiste_joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdiste_joukko.lisaa(b_taulu[i])

        return yhdiste_joukko


    @staticmethod
    def leikkaus(a, b):
        leikkaus_joukko = IntJoukko()
        a_taulu = a.int_listaksi()
        b_taulu = b.int_listaksi()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkaus_joukko.lisaa(b_taulu[j])

        return leikkaus_joukko


    @staticmethod
    def erotus(a, b):
        erotus_joukko = IntJoukko()
        a_taulu = a.int_listaksi()
        b_taulu = b.int_listaksi()

        for i in range(0, len(a_taulu)):
            erotus_joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            erotus_joukko.poista(b_taulu[i])

        return erotus_joukko


    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.taulukko[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.taulukko[self.alkioiden_lkm - 1]) + "}"
            return tuotos
