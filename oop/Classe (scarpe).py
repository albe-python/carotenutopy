class scarpe:
    def __init__(self, marca, modello, data_uscita, prezzo):
        self.marca = marca
        self.modello = modello
        self.data_uscita = data_uscita
        self.prezzo = prezzo

    def Scheda_scarpe(self):
        return f"\nScheda_scarpe\n Marca: {self.marca}\n Numero modello: {self.modello}\n data_uscita: {self.data_uscita}\n prezzo: {self.prezzo}"

AirJordan= scarpe("Jordan", "Air Jordan 1 Chicago", "1985", "1833$")

print(scarpe.Scheda_scarpe(AirJordan))
