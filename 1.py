### Construir una funcion que reciba su nombre como parametro y que lo muestre 5 veces en la pantalla

"""Nombre * 5"""

print("-------------------------------")
print("------Tu nombre 5 veces--------")
print("-------------------------------")

#Input
nombre = input("Dame tu nombre: ") #Se recibe el dato del usuario

#Definition de función
def RepetirNombre(nombre):
    for RepetirNombre in range(5):
        print(nombre)   
RepetirNombre(nombre)