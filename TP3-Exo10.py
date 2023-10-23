# CORREIA William Bachelor 2 Groupe 3 - TP3 Exercice 10

liste = []

nb = int(input("Insérer le nombre de valeurs à saisir : "))
pmt = 0

for i in range(nb):
    liste.append(int(input(f"Insérer le nombre numéro '{i:d}' : ")))

for i in range(nb):
    for j in range(nb):
        if (liste[i] < liste[j]):
            pmt = liste[i]
            liste[i] = liste[j]
            liste[j] = pmt

print("La liste dans l'ordre croissant :", liste)
