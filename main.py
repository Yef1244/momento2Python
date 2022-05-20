from clases.Ciclista import Ciclista

print("")
print("----------------------------- MENÚ -----------------------------------")
print("------------ Ingrese 1 si desea ingresar un ciclista -----------------")
print("-------- Ingrese 2 para mostrar los ciclistas registrados ------------")
print("---- Ingrese 3 para calcular el mejor tiempo entre los ciclistas -----")
print("-------------    Ingrese 0 para cerrar el menú  ----------------------")
print("")

opcion = 1
ciclistas = []
tiempos = []

while(opcion != 0):
    opcion = int(input("Ingrese una opcion: "))
    if(opcion == 1):
        ciclista = Ciclista()
        ciclista.nombre = input("Ingrese el nombre del ciclista: ")
        ciclista.edad = int(input("Ingrese la edad del ciclista: "))
        ciclista.pais = input("Ingrese el país del ciclista: ")
        ciclista.tiempo = int(input("Ingrese el tiempo alcanzado del ciclista: "))
        ciclistas.append(ciclista)
        tiempos.append(ciclista.tiempo)

    elif(opcion == 2):

        for i in ciclistas:
            print(i.nombre)

    elif(opcion == 3):
        tiemposIter = iter(tiempos)
        tiempoRecord = min(tiemposIter)
        print(f"El mejor tiempo fue de {tiempoRecord} minutos")
else:
    print("Se cerró el menú...")