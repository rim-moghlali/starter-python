# rectangle

hauteur = 10
largeur = 3

side = "|"
separator = "-"

for i in range(hauteur):
    if i == 0 or i == hauteur -1:
        separator = "-"
    else:
        separator = " "
    print(side + separator * largeur + side)