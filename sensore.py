class Sensore:
    def __init__(self, codice: str, grandezza: int, u_misura: str, s_max: int):
        self.codice = codice
        self.grandezza = grandezza
        self.u_misura = u_misura
        self.s_max = s_max
        
    def __str__(self):
        print(f"codice: {self.codice}, grandezza: {self.grandezza}, unità misura: {self.u_misura}, soglia massima: {self.s_max}")
        