import os


Participantes=[]
os.system("cls")
nombreFestival = input ("Ingresa el nombre del festival: ")
os.system("cls")
opcion=0


while (opcion !=6):
    Participante={}
    print ("Bienvenido a", nombreFestival,"musical Festival \n")
    print ("************************************\n")
    print ("1) Registrar una agrupacion musical o DJ")
    print ("2) Listado de los participantes que no se han presentado")
    print ("3) Cambiar el estado de un participante")
    print ("4) Modificar la hora de presentacion")
    print ("5) Retirar una agrupacion musical o DJ")
    print ("6) Salir\n")
    opcion = int(input("Digita una opcion: "))

    if opcion==1:
        os.system("cls")
        Participante["id"] = int(input("Digital el id de la agrupacion musical o DJ: "))
        Participante["nombre"] = input("Digita el nomrbre de la agrupacion musical o DJ: ")
        Participante["genero"] = input("Digita el genero musical de la agrupacion o DJ: ")
        Participante["hora"] = input("Digita la hora de la presentacion: ")
        Participante["pago"] = float(input("Digita el pago realizado a la agrupacion o DJ: "))
        Participante["estado"] = False
        Participantes.append(Participante)
        print("\nRegistro exitoso\n")
        os.system("pause")
        os.system("cls")
    elif opcion==2:
        os.system("cls")
        buscarParticipante = int(input("Digita el id de la agrupación o DJ que deseas buscar: "))
        encontrado = False
        for participanteEncontrado in Participantes:
            if participanteEncontrado['id'] == buscarParticipante:
                encontrado = True
                estado = "Presentada" if participanteEncontrado["estado"] else "No Presentada"
                if participanteEncontrado["estado"]:
                    print(f"La banda {participanteEncontrado['nombre']} ya se ha presentado.")
                else:
                    print("\n************************************")
                    print("\nAgrupación encontrada: \n")
                    print(f"id: {participanteEncontrado['id']}")
                    print(f"nombre: {participanteEncontrado['nombre']}")
                    print(f"genero: {participanteEncontrado['genero']}")
                    print(f"hora: {participanteEncontrado['hora']}")
                    print(f"pago: {participanteEncontrado['pago']}")
                    print(f"estado: {estado}\n")
        if not encontrado:
            print(f"No se encontró una banda con el ID {buscarParticipante}")    
        os.system("pause")
        os.system("cls")
    elif opcion==3:
        os.system("cls")
        os.system("cls")
    elif opcion==4:
        print("\nEstas en la opcion 3")
        os.system("cls")
    elif opcion==5:
        print("\nEstas en la opcion 4")
        os.system("cls")
    elif opcion>6:
        os.system("cls")
        print("\nopcion invalida\n")
        os.system("pause")
        os.system("cls")
    else: pass
os.system("cls")
print ("\n************************************\n")
print ("Saliste")
print ("\n************************************\n")