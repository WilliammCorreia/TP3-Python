# CORREIA William Bachelor 2 Groupe 3 - TP3 Exercice 1

liste = []

nb = int(input("Insérer le nombre de valeurs à saisir : "))

for i in range(nb):
    liste.append(int(input(f"Insérer le nombre numéro '{i:d}' : ")))

print("Nombre de la liste :", liste)
