# CORREIA William Bachelor 2 Groupe 3 - TP3 Exercice 9

liste1 = []
liste2 = []

nb = int(input("Insérer le nombre de valeurs à saisir dans les listes : "))

print("\n ****** Première liste ******")
for i in range(nb):
    liste1.append(int(input(f"Insérer le nombre numéro '{i:d}' : ")))

print("\n ****** Deuxième liste ******")
for i in range(nb):
    liste2.append(int(input(f"Insérer le nombre numéro '{i:d}' : ")))

for i in range(nb-1):
    if (liste1[i] != liste2[i]):
        print("\nLes deux listes sont différentes.")
        exit()

print("\nLes deux listes sont identiques.")
