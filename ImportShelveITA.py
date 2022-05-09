import shelve

M = shelve.open( Esempio txt) # open -- file può ottenere suffisso da low level
                           # library

M[key] = data              # memorizza i dati nella chiave (sovrascrive i vecchi dati se
                           # utilizza una chiave esistente)
data = M[key]              # recupera una copia dei dati nella chiave (Va in KeyError
                           # se la chiave non ha valore o non esiste)
del M[key]                 # Cancella i dati salvati nella chiave (Va in KeyError
                           # se la chiave non ha valore o non esiste)

flag = key in M            # true quando la chiave esiste
klist = list(M.keys())     # Una lista di tutte le chiavi esistenti(slow!)

# as M was opened WITHOUT writeback=True, beware:
M['xx'] = [0, 1, 2]        # this works as expected, but...
M['xx'].append(3)          # *this doesn't!* -- M['xx'] is STILL [0, 1, 2]!


# M è stato aperto SENZA Writeback=Vero, attenzione:
M['xx'] = [0, 1, 2]   # questo funziona come previsto, ma...
M['xx']. append(3)   # *questo non è ! * -- M['xx'] è ANCORA [0, 1, 2]!


#  Dopo aver aperto M senza Writeback=True, è necessario pensare attentamente ai passaggi seguenti:
temp = M['xx']   # estrae la copia
temp.append(5)   # muta la copia
M['xx'] = temp   # memorizza la copia, per persistere

# oppure, M=shelve.open(filename, Writeback=True) ti permette da codice
# M['xx']. append(5) di farlo funzionare come previsto, MA sarebbe anche
# consumata più memoria rendono cosi l'operazione M.close() più lenta.

M.close()                  
