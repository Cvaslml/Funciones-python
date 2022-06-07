### Construir una funcion que reciba como parametro una lista de datos numericos y retome la suma de dichos datos

"""Sumatoria de elementos de una lista numerica"""

print("-----------------------------")
print("------Suma de numeros--------")
print("-----------------------------")

#Input
def Listsum(Lista):
    suma = 0
    for i in Lista:
        suma = suma + i
    return suma

Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"La suma es = {Listsum(Lista)}")