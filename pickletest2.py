import pickle
import re





import mysql.connector

import prova1

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mydb = x
mydb is x


# Il modulo PICKlE che il cPIckle implementano un algoritmo di serializzazione degli oggetti 
# Può essere conservato è trasmesso e in secondo tempo ricostruito per riottenere le sue caratteristiche
# cPickle quindi è lo stesso elemento di serializzazione ma in formato nativo C

x= [ 3, 2, 4]

pickle

re.search


pickle.DEFAULT_PROTOCOL

pickle.HIGHEST_PROTOCOL

pickle.Pickler(pickle.DEFAULT_PROTOCOL)

pickle.Pickler.dump(x)

# il controllo

pickle.Pickler.clear_memo()


# dump e dumps 

# load e loads 


#  exception PickleError  exception PicklingError  exception UnpicklingError

pickle.Unpickler


try:
    import cPickle as pickle
except:
    import pickle
import pprint

data = [ pickletest ]
print ('DATI:')
pprint.pprint(data)

data_string = mydb.dump(data)
print ('PICKLE:')
data_string

# alcuni tipi non serializzabili: None, True e False Interi, interi long, numeri in virgola mobile, numeri complessi stringhe normali ed Unicodetuple, liste, insiemi e dizionari contenenti solamente oggetti serializzabilifunzioni definite nella parte iniziale di un modulofunzioni built-in definite nella parte iniziale di un modulo

# sui può cercare di limitare questa problematica utilizzando exception Pickling Error 

f = open("demofile.txt")

#"r"- Lettura - Valore predefinito. Apre un file per la lettura, errore se il file non esiste

#"a"- Aggiungi - Apre un file per l'accodamento, crea il file se non esiste

#"w"- Scrivi - Apre un file per la scrittura, crea il file se non esiste

#"x"- Crea - Crea il file specificato, restituisce un errore se il file esiste

import marshal
import pickle
import json

y = open("D:\\myfiles\welcome3.txt", "w")

f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

f = open("demofile2.txt", "r")
print(f.readline())

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

fletto= f.read

f = json.dumps(y, indent=5)

h = json.loads(fletto)
print(h)

# Creare un sistema che dopo aver accetato un imput lo scriva su in file e ripeta
# , alla fine lo convertirà in json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))








import shelve

d = shelve.open(filename) # open -- file che può prendere un suffisso 
                          # aggiunto da una libreria di basso-livello

d[key] = data   # immagazzina i dati della chiave (sovrascrive i
                # vecchi dati se sta usando una chiave esistente)
data = d[key]   # recupera una COPIA dei dati dalla chiave
                # (solleva KeyError se la chiave non corrisponde)
del d[key]      # cancella i dati immagazzinati nella chiave 
                # (solleva KeyError se la chiave non corrisponde)
flag = d.has_key(key)   # vero se la chiave esiste
list = d.keys() # una lista di tutte le chiavi esistenti (lento!)

# visto che d è stata aperta SENZA writeback=True, si faccia attenzione che:
d['xx'] = range(4)  # questa lavora come sperato, ma ...
d['xx'].append(5)   # *questa no!* -- d['xx'] è ANCORA range(4)!!!
# avendo aperto d senza writeback=True, avete bisogno di scrivere accuratamente:
temp = d['xx']      # estrae la copia
temp.append(5)      # modifica la copia
d['xx'] = temp      # memorizza la copia, per renderla persistente
# oppure, d=shelve.open(nomefile,writeback=True) potrebbe lasciarvi
# scrivere d['xx'].append(5) e farla funzionare come deisderato, MA
# potrebbe anche consumare una maggiore quantità di memoria, e rendere 
# l'operazione d.close() più lenta. 


d.close()       # chiude d






 
def carica_dati():
    try:
        #infile = open('dati.txt','r')
        namefile = input('Inserire il nome del file e la sua estensione: ')
        infile = open(namefile,'r')
        dati = infile.readlines()
        infile.close()
    except Exception as err:
        dati = list()
        print("File non esistente")
        return dati
    else:
        return dati
 
def carica_liste(dati):
    nominativi = list()
    ore= list()
    for i in range(0,len(dati),2):
        nominativi.append(dati[i].rstrip('\n'))
        ore.append(float(dati[i+1].rstrip('\n')))
    return nominativi, ore
 
def carica_dizionari(n, o):
    d = dict()
    for i in range(0,len(n)):
        d[n[i]] = o[i]
    return d
 
def salva_dizionario(d):
    file = open('log.dat','wb')
    pickle.dump(d, file)
    file.close()
 
def visualizza_info(d, paga_oraria):
    for key in d:
        totale = d[key]*paga_oraria
        print("Nominativo dipendente: "+key+"\t"+ str(d[key]) + " ore lavorate\t Costo orario: "+str(paga_oraria)+ "€\t Paga lorda € "+str(totale))
 
 
def main():
    dati = carica_dati()
    if (len(dati)>0):
 
        try:
 
            nominativi, ore = carica_liste(dati)
 
            monte_ore_lav = carica_dizionario(nominativi, ore)
 
            paga_oraria = float(input('Inserire la paga oraria in Euro: '))
 
            salva_dizionario(monte_ore_lav)
            visualizza_info(monte_ore_lav, paga_oraria)
 
        except Exception as err:
            print(err)
 
main()