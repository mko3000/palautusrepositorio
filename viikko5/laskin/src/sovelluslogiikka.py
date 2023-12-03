class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._historia = []

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi
        self._tallenna_tila()

    def plus(self, operandi):
        self._arvo = self._arvo + operandi
        self._tallenna_tila()

    def nollaa(self):
        self._arvo = 0
        self._tallenna_tila()

    def aseta_arvo(self, arvo):
        self._arvo = arvo
        self._tallenna_tila()

    def arvo(self):
        return self._arvo
    
    def kumoa(self):
        if len(self._historia) <= 1:
            self._arvo = 0
            return
        self._historia.pop()
        self._arvo = self._historia[-1]
    
    def _tallenna_tila(self):
        self._historia.append(self._arvo)