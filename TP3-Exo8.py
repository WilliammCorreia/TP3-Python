# CORREIA William Bachelor 2 Groupe 3 - TP3 Exercice 8

liste = []
pmt = 0
longueur = 0

nb = int(input("Insérer le nombre de valeurs à saisir : "))

for i in range(nb):
    liste.append(input(f"Insérer la lettre numéro '{i:d}' : "))

pmt = liste[len(liste)-1]
longueur = len(liste)-1

for i in range(len(liste)-1):
    liste[longueur] = liste[longueur-1]
    longueur -= 1

liste[0] = pmt

print("La liste decalé vers la droite :", liste)
