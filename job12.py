# ouvrir le fichier
file = open("data.txt", "r")
# lire le fichier
data = file.read()
#compter les mots dans le fichier
words = data.split()
print ("Le nombre de mots est: ", len(words))