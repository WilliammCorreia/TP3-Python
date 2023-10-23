# CORREIA William Bachelor 2 Groupe 3 - TP3 Exercice 7

liste = []

nb = int(input("Insérer le nombre de valeurs à saisir : "))

for i in range(nb):
    liste.append(int(input(f"Insérer le nombre numéro '{i:d}' : ")))

for i in range(len(liste)-1):
    if (liste[i] > liste[i+1]):
        print("\nLa liste n'est pas triée dans l'ordre croissant.")
        exit()
    else:
        print("\nLa liste est triée dans l'ordre croissant.")
        exit()
