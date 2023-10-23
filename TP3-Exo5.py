# CORREIA William Bachelor 2 Groupe 3 - TP3 Exercice 5

liste = []
occurrence = []
x = 0

nb = int(input("Insérer le nombre de valeurs à saisir : "))

for i in range(nb):
    liste.append(int(input(f"Insérer le nombre numéro '{i:d}' : ")))
    occurrence.append(0)

for i in range(nb):
    x = i
    for j in range(nb-i-1):
        if (liste[i] == liste[(x+1)]):
            if (occurrence[i] != -1):
                occurrence[i] += 1
                occurrence[(x+1)] = -1
        x += 1

print("\n")

for i in range(nb):
    if (occurrence[i] >= 1):
        print("La valeur '%d' est présente %d fois." %
              (liste[i], (occurrence[i]+1)))
        x = "aucun"

if (x != "aucun"):
    print("Il n'y pas d'occurrence dans le tableau.")
