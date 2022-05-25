#  3 le regole fondamentali OOP

#  Ereditarierà  Polimorfismo  Incapsulamento   ASTRAZIONE 

#  Pyt. è un linguaggio debolmenete tipizzato.  Definizione non tecnica:  Non tipizzato

#  Polimorfismo per inclusione: la dove un tipo non è neccesario non viene utilizzato

#  Variabili

from copyreg import pickle
from msilib.schema import Class


  


numero = 10         # non interessa a python che tipo di valore tu contega
numero =  0        # quando un valore è null o indefinito o 0 l'unico valore che ha è False

#   UN LIVELLO DI ASTRAZIONE DEL POLIMORFISMO
#   ogni oggetto in python che può avere un valore, accetta controlli booleani, 
#   avendo una tipizzazione debole non importa se è o non è un booleano python 
#   comunque andare andare a copntrollarlo tramite il suo valore reale 

numero != True
   
stringa = "Python"   #  questa variabile la uso in metodo x
numero = "mirko"
 
nomelista = [1, 2, 3, stringa, "mirko", True, numero ]

print( "mirko" , nomelista )
print(nomelista)




#  input : parametro in ingresso richiesto al utente 
#  funzione di basso livello ma e comunque una delle più costose 
#  tiene in run time i valori delle azioni 

#Scelta = input('dimmi il tuo nome')  # = assegnazione

#print(Scelta == "mirko")   # ==  controllo, uguaglianza fa si che stampi true 
#print(Scelta != "mirko")   # Diverso da, falso rispetto a, uguaglianza fa si che stampi false

Scelta = 1

if Scelta == 3:
  Scelta2 = input('fai la tua scelta digita o yes o no\n')
  
  

# IF è il Blocco basilare di condizione la sintassi che si usa è [ if condizione : /n blocco di codice  ]
# Else quindi e l'alternativa alla condizione if iniziale nel caso non sia verificata 


#  Ereditarierà - Classi

# Una classe è un modello di riferimento per la creazione di un oggetto

class primaclasse ():

    x = 0
    y= "mirko"
    m= "nonna"
    b= True


print(primaclasse().x)
valoredelloggetto = primaclasse()
print(valoredelloggetto.y)


#  l'oggeto è insieme i valori e metodi datagli dalla classe di riferimento 
#  e il valore e solo l'elemento che compone la veridicità della variabile

i = 0

o = primaclasse()


class primaEredità (): 
    
    def __init__(self, name, age):
      self.y1 = name
      self.m1 = age

    x1 = 0
    y1= "mirko"
    m1= "nonna"
    b1= True

    def sommatore ():      
# METODI SONO LE AZIONI PRATICHE CHE PUò COMPIERE IL NOSTRO CODICE O IL NOSTRO OGGETTO
        x1 +=100
        print(x1)

class secondEredità (primaEredità):
    x1 = 100
    
    primaEredità.sommatore



# __init__ definisce l'insieme delle caraterische che danno corpo, valore, e in caso anche metodi, i me e costituiscono l'oggetto
# self 

# Incapsulamento: è la capacità del codice di nascedersi e nascodere pezzi di se stesso alla sua comprensione

class Person:
   
  età = 10

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def mirko (self):
    print(self.name, self.age)

class Studente (Person):
 

 def __init__(self, name, age, anno ):
     super().__init__(name, age) 
     scuola = "quinto alberti"
     self.scuola = scuola
     self.anno = anno
 def welcome (self):
     print("Ciao", self.name, " all'età di ", self.age, " sei il bevenuto alla ", self.scuola)

class AiutoBidello (Person):
 

  def __init__(self, name, age):
      Studente()
      super().__init__(name, age)
      self.stipendio = 100
      self.scuola = "mirko"


p1 = Person("John", 36)

p3 = Studente("carlo", 22, 1995  )

p3.welcome


del p1.age    # è il commando per eliminare un'attributo 

p1.age = 20    # il comando per dare un valore a quel elemento

del p1     # è il commando per eliminare l'oggeto

class Person2:
  pass     # è un comando per evitare che una classe vuota vada in errore

Person2()


class creadict:
  car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
 }
 



pickle



