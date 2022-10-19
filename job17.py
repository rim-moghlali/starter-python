def myfunction( *args):
    myList = []
    
    for i in args:
        myList += [i]
    for j in range(len(myList)):
# len pour parcourir le fichier en entier
        if (myList[j] % 2 ) == 0:
            print(myList[j])
myfunction(5,8,6,9,25,26)