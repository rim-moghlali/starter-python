# parcourir les nombres entiers de 1 à 100
for i in range(0,100):
# cette condition permet d'afficher les multiples de 3 et 5
# le % veut dire que le reste est 0
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)