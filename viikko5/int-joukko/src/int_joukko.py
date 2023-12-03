KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = self.tarkasta_syote(kapasiteetti)
        self.kasvatuskoko = self.tarkasta_syote(kasvatuskoko)
        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0
    
    def tarkasta_syote(self, syote):
        if not isinstance(syote, int) or syote < 0:
            raise Exception("Väärä kapasitetti")
        else:
            return syote
        
    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm == len(self.ljono):
                self.laajenna_listaa()
            return True
        return False

    def poista(self, n):

        if not self.kuuluu(n):
            return False

        poistettava_indeksi = 0
        while self.ljono[poistettava_indeksi] != n:
            poistettava_indeksi += 1

        for i in range(poistettava_indeksi, self.alkioiden_lkm):
            self.ljono[i] = self.ljono[i+1]

        self.ljono[self.alkioiden_lkm] = 0
        self.alkioiden_lkm -= 1
        return True

    def kopioi_lista(self, kopioitava_lista, uusi_lista):
        for i in range(0, len(kopioitava_lista)):
            uusi_lista[i] = kopioitava_lista[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]
    
    def laajenna_listaa(self):
        kopioitava_lista = self.ljono
        self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(kopioitava_lista, self.ljono)

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
