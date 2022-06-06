import pickle
import re


x= [ 3, 2, 4]

pickle

re.search


pickle.DEFAULT_PROTOCOL

pickle.HIGHEST_PROTOCOL

pickle.Pickler(pickle.DEFAULT_PROTOCOL)

pickle.Pickler


pickle.Unpickler




















 
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
 
def carica_dizionario(n, o):
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