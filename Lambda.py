











# LAMBDA è UN MODO PER ANONIMIZARE e Snellire gli formule matematiche pure 


#   lambda arguments :  expression



c = lambda a : a + 10     #   il lato destro è il cosa fa 
print(c(5))

y = lambda a, b, c : a + b + c
print(y(5, 6, 2))

x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
  c = lambda a : a * n


print(c(11))







class MANAGER:

    lista = ()

    def __init__(self):
        self.__stipendio = 1230
        self.__VALORE = " mirko "
        
    def Paga(self):
        print("La MANAGER è pagato {}".format(self.__stipendio))

    def impostastipendio(self, variante):
        self.__stipendio = variante

    def impostavqalore ( self, variante2 ):
        self.__VALORE = variante2
    
    def ValorePrint(self):
       print( "IL tuo valore è {}".format(self.__VALORE) )

    def creafilio(self, variabile):
      self.variabile = Figlio()


class Figlio (MANAGER):
 
 def __init__(self):
    super().__init__()
 
# istanza di classe
x = MANAGER()
x1 = MANAGER()

print(x)
print(x1)

y = input()
# funzione setter
x.impostastipendio(y)
x.impostavqalore("MirkoSuper")
x.ValorePrint()

x.__stipendio = 100     # non ha alcune valore per x e per manager
x.Paga()
x1.Paga()
