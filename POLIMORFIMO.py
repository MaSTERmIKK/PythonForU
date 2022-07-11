DIZIO = {
  "Marca": "Nike",
  "Modello": "air jordan",
  "Anno": 1999
}

print(DIZIO)


# Incapsulamento in Python
class Facciata:

    def __init__(self):
        self.__colore = "verde"

    def colora(self):
        print("La facciata è di colore {}".format(self.__colore))

    def impostaColore(self, variante):
        self.__colore = variante

# istanza di classe
x = Facciata()
x.colora()

# modifica del colore
x.__colore = "rosso"
x.colora()

# funzione setter
x.impostaColore("rosso")
x.colora()