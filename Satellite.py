

class Satellite:
    def __init__(self, nome):
        self.nome = nome
        self.sensori = {}
        self.letture = []
        
    def aggiungi_sensore(self, sensore):
        if sensore.codice in self.sensori:
            raise ValueError("Codice sensore già presente")
        self.sensori[sensore.codice] = sensore
        
    def registra_lettura(self, codice_sensore , valore):
        if not codice_sensore in self.sensori:
            raise ValueError("Codice non presente nel satellite")
        sensore = self.sensori[codice_sensore]
        self.letture.append({
            "sensore": codice_sensore,
            "grandezza": sensore.grandezza,
            "valore": valore,
            "unità": sensore.u_misura,
            "allareme": valore > sensore.s_max
        })
    def oltre_soglia(self):
        allarmati = []
        if not self.letture:
            print("Nessuna lettura")
            
        for lettura in self.letture:
            if lettura["allarme"]:
                allarmati.append(lettura)
        return allarmati
    
    def riepilogo(self):
        allarmi = self.oltre_soglia()
        for allarme in allarmi:
            print(f"codice: {allarme['sensore']}, lettura: {allarme['valore']}, unità: {allarme['unità']},stato: ALLARME")
            
        
