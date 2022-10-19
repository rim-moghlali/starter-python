# l utilisateur saisi un texte
saisi = input("texte : ")
# creation d un fichier output.txt et ecrire dedans la saisie de l utilisateur
fichier = open("output.txt" , "w")
fichier.write(saisi)
fichier.close()
# ouvrir le fichier et afficher son contenu sur le terminal
fichier = open("output.txt", "r")
print(fichier.read())
fichier.close()