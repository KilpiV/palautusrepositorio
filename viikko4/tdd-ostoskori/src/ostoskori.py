from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = []
        self.tuotemaara = 0
        self.summa = 0
        pass
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):   
        return self.tuotemaara
        pass
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return self.summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        loytyi = False
        for ostos in self.kori:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                loytyi = True
        if not loytyi:
            self.kori.append(Ostos(lisattava))
        self.tuotemaara += 1
        self.summa += lisattava.hinta()
        pass

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.kori:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                self.tuotemaara -= 1
                self.summa -= poistettava.hinta()
                if ostos.lukumaara() == 0:
                    self.kori.remove(ostos)
                break
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        self.kori = []
        self.summa = 0
        self.tuotemaara = 0
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kori
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
