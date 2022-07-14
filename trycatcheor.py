


# TRY E Execpt SySTEM e comando or e and e is

# Il try catch e un blocco di codice che si occupa di gestire le eccezioni
# Ricordate non esiste un modo di conprovare l'assenza totale di errori am solo di evidenziarne uno conosciuto 




try:
  print(x)
except:
  print("OPS WE HAVE A PROBLEM")



try:
  print(x)
except NameError:
  print("VariabIle ANndrea VUOTA ")
except TypeError:
  print("OPS WTF")
except:
    print(" wtf ")
else:     # viene eseguito quando non abbiamo errori
    print("non ci sono eroi")
finally:   # viene stampato comunque sempre
    print("ok 2")


x1 = "pippo"

try:
  print(x1)
except:
  print("Non funziona pippo")
finally:      # il finaly verrà sempre eseguito indipendetemente dal risultato del blocco try catch
  print("The 'try except' is finished")



x2= 2

#IS, is not, not , AND E OR sono i tre operatori logici complessi più utilizati 

if not( x2 <=0 ):   # situazioni matematiche 
    print("pippo")


if x1 is "pippo":
    print("w mikk")

if x1 is not "pippo":
    print("w mikk4")

  
if x1 is "pippo" or x2 == 1 or x2 == "mirko":    # OR CI DICE CHE BASTA CHE UNA DELLE DUE O PIù CONDIZIONI SIANO VERE
    print("w mikk2")

if x1 is "pippo" and x2 == 1:    # AND CI DICE CHE SERVIRANNO ENTRAMBE LE CONDIZIONI VERE 
    print("w mikk3")


# la differenza fra == è  l'IS  E CHE SI PUò USARE ANCHE SUGLI OGGETTI