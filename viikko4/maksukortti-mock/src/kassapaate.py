HINTA = 5


class Kassapaate:
    def __init__(self):
        self.myytyja_lounaita = 0

    def lataa(self, kortti, summa):
        kortti.lataa(summa)
        if summa < 0:
            return 
        kortti.saldo += summa

    def osta_lounas(self, kortti):
        if kortti.saldo < HINTA:
            return False
        kortti.osta(HINTA)
        self.myytyja_lounaita = self.myytyja_lounaita + 1
