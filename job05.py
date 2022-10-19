# l utilisateur saisie les valeurs 1 et 2 
a = int(input("Valeur 1 : "))
b = int(input("Valeur 2 : "))
# je met range pour afficher les nombres entre les valeurs saisies par l utilisateur
for a in range(a+1,b):
    print(a)
# la fonction reversed pour afficher les nombres decroisants
for b in reversed(range(b+1,a)):
    print(b)
# pour l affichage des nombres negatifs
for a in range(a-1,b):
    print(a)

for b in reversed(range(b-1,a)):
    print(b)