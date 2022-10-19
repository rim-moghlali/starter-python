# demander l'age à l'utilisateur et le recuperer
age = int(input("Bonjour, quel âge as tu ?"))
# mettre une condition pour afficher le commentaire sur l'age de l utilisateur
if age >= 18:
    print ("Tu es majeur")
elif age > 0 and age < 18:
    print ("Tu es mineur")
else:
    print("vous n'êtes pas née!")