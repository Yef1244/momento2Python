from clases.Cliente import Cliente

print("")
print("------------------------- BANCO DE HIERRO --------------------------------")
print("----- Ingrese 1 si desea ingresar un cliente e informacion de cuenta -----")
print("------------------ Ingrese 2 para consultar el saldo ------------------")
print("-------------- Ingrese 3 para ingresar o retirar dinero ----------------")
print("-------------    Ingrese 0 para cerrar el menú  ----------------------")
print("")

opcion = 1
clientes = []
saldos = []

while(opcion != 0):
    opcion = int(input("Ingrese una opcion: "))
    if(opcion == 1):
        cliente = Cliente()
        cliente.nombre = input("Ingrese el nombre del cliente: ")
        cliente.apellido = input("Ingrese el apellido del cliente: ")
        cliente.cedula = int(input("Ingrese la cedula del cliente: "))
        cliente.ciudad = input("Ingrese la ciudad del cliente: ")
        cliente.nroCuenta = int(input("Ingrese el número de cuenta: "))
        cliente.saldo = float(input("Ingrese el saldo: "))
        clientes.append(cliente)
        saldos.append(cliente.nroCuenta)
        saldos.append(cliente.saldo)

    elif(opcion == 2):
        print(f'El número de cuenta es {saldos[0]} con un saldo de: ${saldos[1]}')

    elif(opcion == 3):
        opcion2 = input("Digite \"ingresar\" o \"retirar\": ")
        if(opcion2 == "ingresar"):
            ingreso = float(input("¿Cuanto dinero desea ingresar?: "))
            suma = saldos[1] + ingreso
            saldos[1] = suma

        elif(opcion2 == "retirar"):
            retiro = float(input("¿Cuanto dinero desea retirar?: "))
            if(retiro <= saldos[1]):
                resta = saldos[1] - retiro
                saldos[1] = retiro
            else:
                print("no tiene saldo suficiente")

else:
    print("Se cerró el menú...")
