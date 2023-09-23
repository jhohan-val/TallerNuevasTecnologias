import os


Participantes=[]
os.system("cls")
nombreFestival = input ("Ingresa el nombre del festival: ")
os.system("cls")
opcion=0


while (opcion !=5):
    Participante={}
    print ("Bienvenido a", nombreFestival,"musical Festival \n")
    print ("************************************\n")
    print ("1) Registrar una agrupacion musical o DJ")
    print ("2) Listado de los participantes")
    print ("3) Modificar la hora de presentacion")
    print ("4) Retirar una agrupacion musical o DJ")
    print ("5) Salir\n")
    opcion = int(input("Digita una opcion: "))

    if opcion==1:
        os.system("cls")
        Participante["id"] = int(input("Digital el id de la agrupacion musical o DJ: "))
        Participante["nombre"] = input("Digita el nomrbre de la agrupacion musical o DJ: ")
        Participante["genero"] = input("Digita el genero musical de la agrupacion o DJ: ")
        Participante["hora"] = input("Digita la hora de la presentacion: ")
        Participante["pago"] = float(input("Digita el pago realizado a la agrupacion o DJ: "))
        Participante["estado"] = input("La agrupacion o DJ ya se presento? si o no: ")
        Participantes.append(Participante)
        print("\nRegistro exitoso\n")
        os.system("pause")
        os.system("cls")
    elif opcion==2:
        os.system("cls")
        print("\n", Participantes, "\n")
        os.system("pause")
        os.system("cls")
    elif opcion==3:
        print("\nEstas en la opcion 3")
        os.system("cls")
    elif opcion==4:
        print("\nEstas en la opcion 4")
        os.system("cls")
    elif opcion>5:
        os.system("cls")
        print("\nopcion invalida\n")
        os.system("pause")
        os.system("cls")
    else: pass
os.system("cls")
print ("\n************************************\n")
print ("Saliste")
print ("\n************************************\n")