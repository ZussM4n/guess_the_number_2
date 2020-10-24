import random
from guess_the_number_functions import *

intentos = 0
maximo = 0
clave = 0

intentosMax = int(input("¿How many tries do you want?: "))
maximo = int(input("Say me the maximun number: "))
clave= random.randint(1, maximo)

while True:
    intentos += 1
    if intentos > intentosMax:
        print("You have no more tries left")
        end_of_game()
        break
    
    prueba = int(input("Guess the number!"))

    if clave == prueba:
        print("¡You win!",clave)
        you_win()
        break
    
    elif clave > prueba:
        print("It's a higher number")
        
    else:
        print("It's a lower number")
        