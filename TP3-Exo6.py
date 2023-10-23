# CORREIA William Bachelor 2 Groupe 3 - TP3 Exercice 6

liste = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 0]
valeur = 0
pmt = 0
longueur = len(liste)-1

valeur = int(input("Insérer une valeur à ajouter dans la liste : "))

for i in range(len(liste)-1):
    if (liste[i-1] < valeur and liste[i] > valeur):
        for j in range((len(liste)-1) - i):
            liste[longueur] = liste[longueur-1]
            longueur -= 1
        liste[i] = valeur
    elif (liste[len(liste)-2] < valeur):
        liste[len(liste)-1] = valeur
    elif (liste[0] > valeur):
        for j in range((len(liste)-1) - i):
            liste[longueur] = liste[longueur-1]
            longueur -= 1
        liste[i] = valeur


print("La liste triée :", liste)
