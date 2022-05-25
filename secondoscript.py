
#   Benvenuti alla seconda lezione 

from asyncio.windows_events import NULL
from cgi import print_arguments
from ftplib import parse227


def mirko ():
    print("qui non c'è")
def mirkocè ():
    print(x + " grazie di aver usato la nostra app ")


#  Iniziamo a parlare ora di LOOP e/o ITERATORI

#   Sono uno degli elementi più complessi da inserire senza trouble shotting
#   Un motivo di persistere una ending condition

#  While  ripete ed Esegue un insieme di condizioni purchè la condizione sia vera

thisdict = {
  "brand" : "mirko",
  "model" : "Mustang",
  "year": 1969,
  "years": 1900
}

i = input( "che operazione vuoi fare?  aggiungi / stampa /esci " )
i2 = 0

while i2 >= 1:

 #While i != NULL:

  while i != "esci":
  
   # Menu uno

    if i == "stampa":
       print(thisdict)
       i = input( "che operazione vuoi fare?  aggiungi / stampa /esci " )

    if i == "aggiungi":
       thisdict["color"] = "red"  # aggiungere dovremmo dare la scelta in input
       i = input( "che operazione vuoi fare?  aggiungi / stampa /esci " )

    if i == "esci":
      break
  else:
   i = input( "sei sicuro? yes/no" )
   if i == "si":
     i2 +=1
   if i == "no":  
     i = input( "che operazione vuoi fare?  aggiungi / stampa /esci " )

print("grazie mille")
 
 
 # INFINITI










#  For il primo loop che andiamo a vedere 

Frutto = input("inseristi il frutto che cerchi")   # input tipo frutto da cercare

 #  mai il raw input se non è strettamente neccesario

listo = [ mirko, x2 ]
listo1 = 1

fruits = ["apple", "mirko", "banana", "cherry", 5, "ciliegia", Frutto, listo]      # iniziano a esssere numerati partendo da 0 

for x in fruits:
  print(x)
  if x == Frutto: 
         # va tutto bene
      break
  if x != Frutto: 
      mirko()
      
print(Frutto)
  
m= ""     # False 
m= 0      # False
m= NULL   # False
m= False  # false

#  Valori booleani in py sonos empre veri e controllabili su qualsiasi elemento
#  A due condizioni che il valore non sia 0 o che la variabile non abbia valore

exp = 0
mikk = 0

print(exp + " hai questa exp  ")   # non ci interessa del tipo









#     Set è uno dei 4 tipi di dati integrati in Python utilizzati per archiviare raccolte di dati, 
#     gli altri 3 sono List , Tuple e Dictionary , tutti con qualità e utilizzo diversi.


thisset = {"apple", "banana", "cherry"}
print(thisset)


thislist = ["apple", "banana", "cherry", "banana"]
print(len(thislist))


thistuple = ("apple", "banana", "cherry")
print(thistuple)



thisdict = {
  1 : thislist,
  "model" : "Mustang",
  "year": 1969,
  "years": 1900
}

print(thisdict)
print(thisdict["model"])
print(len(thisdict))
print(type(thisdict))

thisdict["color"] = "red"  # aggiungere
thisdict["year"] = 2028 # modifica diretta
thisdict.update({"color": "red"}) # modifica indiretta
del thisdict["model"]   # cancellazione totale 
thisdict.pop("model")   # rimozione dell'elemento chiave valore
thisdict.clear()        # svuota l'elemento dict

x = thisdict.items()  # stampa lista chiavi e valore

if "model" in thisdict:  # controllo di esistenza delle chiavi
  print("Yes, 'model' esiste")

for x , y in thisdict.items:    # cicla e stampa le chiavi su variabili separate richiamabili
  print(x, y)


import Padre


p = 0

p2 = 0

Padre.creadict(p)

Padre.creadict.car.update({"color": "red"})


Padre.creadict(p2)


thisdict["anthoer dict"] = p # modifica diretta


