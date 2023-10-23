# CORREIA William Bachelor 2 Groupe 3 - TP3 Exercice 3

liste = []
moyenne = 0

nb = int(input("Insérer le nombre de valeurs à saisir : "))

for i in range(nb):
    liste.append(int(input(f"Insérer le nombre numéro '{i:d}' : ")))
    moyenne += (liste[i]/nb)

print(f"\nLa moyenne de la liste est de : {moyenne:.2f}")
