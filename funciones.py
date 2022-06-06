"""Buscar un numero en conjunto"""

print("------------------------------------------")
print("------BUSCAR UN NUMERO EN CONJUNTO--------")
print("------------------------------------------")
#Input
b = int(input("Numero a buscar:")) #Se recibe el dato del usuario

#Processing
a =[1,2,3,4,5] #Se almacena una lista de datos
r = False #Se inicia la variable r con un valor falso

for i in a:
    if i == b:
        print("Lo encontre")
        r = True
if r == False:
    print("No lo encontre")

#Output
print("\nY hubo un final ruin")

