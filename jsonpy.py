import json      # IMPORTIAMO LA LIBRERIA JSON ALTRIMENTI NON ANDRà NULLA


# RICEVERE UN JSON:
x =  '{ "Nome":"Mirko", "Età":36, "Città":"Old York"}'

# caricare l'elemento x:
y = json.loads(x)

#il risultato sarà un Python dictionary:
print(y["Età"])



#inviare e creare un json
# ora abbiamo l'oggetto (dict):
x1 = {
  "Nome": "Micheal",
  "Valore": 28,
  "Stile": "old london"
 }

# convertire in  JSON:
y1 = json.dumps(x1)

# il risultato sarà un JSON in string:
print(y1)


# Ecco i tipi convertibili 

# # dict
# # list
# # tupla
# # int
# # float
# # Vero
# # Falso
# # none


# # Utilizzare il indent parametro per definire il numero di rientri:

json.dumps(x, indent=4)

# # Utilizzo del separatore per modificare il separatore predefinito:

u = {
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

# facilità la lettura:
print(json.dumps(u, indent=6))


json.dumps(u, indent=4, sort_keys=True)    # Sort_Key può ordinare automaticamente un elemento quando scrivimo o leggiamo un dato
print(u)