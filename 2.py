### Construir una funcion que reciba una cadena digitada (cómo parametro) por el usuario y que lo muestre n veces en la pantalla. El valor de n tambien digitado por el usuario

"""Frases graciosas que hacen reir"""

print("------------------------------------")
print("------Frase repetida n veces--------")
print("------------------------------------")

#Input
Frase = input("Dame una frase: ") #Se recibe el dato del usuario
n = int(input("¿Cuantas veces quieres que se repita?: "))

#Definition de función
def RepetirFrase(Frase):
    for RepetirFrase in range(n):
        print(Frase)   
RepetirFrase(Frase)