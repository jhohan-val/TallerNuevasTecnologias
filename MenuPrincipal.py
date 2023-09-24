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
    print ("1) Registrar una agrupacion musical")
    print ("2) Listado de los participantes que no se han presentado")
    print ("3) Cambiar el estado de un participante")
    print ("4) Modificar la hora de presentacion")
    print ("5) Retirar una agrupacion musical")
    print ("6) Salir\n")
    opcion = int(input("Digita una opcion: "))

    if opcion==1:
        os.system("cls")
        Participante["id"] = int(input("Digital el id de la agrupacion musical: "))
        Participante["nombre"] = input("Digita el nomrbre de la agrupacion musical: ")
        Participante["genero"] = input("Digita el genero musical de la agrupacion : ")
        Participante["hora"] = input("Digita la hora de la presentacion: ")
        Participante["pago"] = float(input("Digita el pago realizado a la agrupacion : "))
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
                    print(f"\nLa banda {participanteEncontrado['nombre']} ya se ha presentado.\n")
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
            print(f"\nNo se encontró una agrupacion con el ID {buscarParticipante}\n")    
        os.system("pause")
        os.system("cls")
    elif opcion==3:
        os.system("cls")
        cambiarEstado = int(input("Ingrese el ID de la banda cuyo estado desea cambiar: "))
        encontrada = False
        for Estado in Participantes:
            if Estado["id"] == cambiarEstado:
                encontrada = True
                if Estado["estado"]:
                    print(f"\nLa banda {Estado['nombre']} ya se ha presentado. No se puede cambiar su estado.")
                else:
                    Estado["estado"] = True
                    print(f"\nEl estado de la banda {Estado['nombre']} ha sido cambiado a 'Presentada'.\n")
                break
        if not encontrada:
            print(f"\nNo se encontró una agrupacion con el ID {cambiarEstado}.\n")
        os.system("pause")
        os.system("cls")
    elif opcion==4:
        os.system("cls")
        cambiarHora = int(input("Ingrese el ID de la banda cuya hora desea cambiar: "))
        encontrada = False
        for hora in Participantes:
            if hora["id"] == cambiarHora:
                encontrada = True
                if hora["estado"]:
                    print(f"\nLa agrupacion {hora['nombre']} ya se ha presentado. No se puede cambiar la hora.\n")
                else:
                    nuevaHora = input("\nDigite la nueva hora de la presentación: ")
                    hora["hora"] = nuevaHora
                    print(f"\nLa hora de presentación de la agrupacion {hora['nombre']} ha sido cambiada a {nuevaHora}.\n")
                break
        if not encontrada:
            print(f"\nNo se encontró una agrupacion con el ID {cambiarHora}.\n")
        os.system("pause")
        os.system("cls")
    elif opcion==5:
        os.system("cls")
        retirarParticipante = int(input("Ingrese el ID de la banda que desea retirar: "))
        encontrada = False
        
        copiaParticipantes = Participantes.copy()
        for retirar in copiaParticipantes:
            if retirar["id"] == retirarParticipante:
                encontrada = True
                if retirar["estado"]:
                    print(f"\nLa agrupación {retirar['nombre']} ya se ha presentado. No se puede retirar.\n")
                else:
                    Participantes.remove(retirar)
                    print(f"\nLa agrupación {retirar['nombre']} ha sido retirada del listado.\n")
        if not encontrada:
            print(f"\nNo se encontró una agrupación con el ID {retirarParticipante}.\n")
        os.system("pause")
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