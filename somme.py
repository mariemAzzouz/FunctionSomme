def somme_nombres_pairs(liste):
    somme = 0
    for nombre in liste:
        if nombre % 2 == 0:
            somme += nombre
    return somme


ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultat = somme_nombres_pairs(ma_liste)
print("La somme des nombres pairs de la liste est :", resultat)