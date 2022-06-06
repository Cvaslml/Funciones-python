"""Buscar un numero en conjunto"""

print("------------------------------------------")
print("------BUSCAR UN NUMERO EN CONJUNTO--------")
print("------------------------------------------")
#Definition of funtion
def buscarDatoEnLista(datoABuscar, lista):
    r = False
    for i in lista:
        if i == datoABuscar:
            r = True
    return r

#Input
dato = int(input("Numero a buscar: ")) #Se recibe el dato del usuario

#Processing
lista =[1,2,3,4,5] #Se almacena una lista de datos
if buscarDatoEnLista(dato, lista):
    print("lo encontre")                         #Con funcion
else:
    print("No lo encontre")

#Output
print("\nY hubo un final ruin")

