# CORREIA William Bachelor 2 Groupe 3 - TP3 Exercice 4

liste = []

nb = int(input("Insérer le nombre de valeurs à saisir : "))

for i in range(nb):
    liste.append(int(input(f"Insérer le nombre numéro '{i:d}' : ")))

valeur = int(input("Insérer la valeur à rechercher : "))

for i in range(nb):
    if (valeur == liste[i]):
        print("\nLe chiffre '%d' est à la case '%d' de la liste." %
              (liste[i], i))
        exit()

print("\nLa valeur n'a pas été trouvé dans la liste.")
