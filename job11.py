# ouvrir le fichier
fichier = open("domains.xml", "r") 
# lire le fichier
domaine = fichier.read()
# compter le nombre du mot de domaine
occurences = domaine.count("domain")
print ('Le nombre des domaines est : ', occurences)