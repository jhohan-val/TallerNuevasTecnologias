

nombreFestival = input ("Ingresa el nombre del festival: ")
opcion=0

print ("Bienvenido a", nombreFestival,"musical Festival \n")

print ("************************************\n")
print ("1) Registrar una agrupacion musical o DJ")
print ("2) Listado de los participantes")
print ("3) Modificar la hora de presentacion")
print ("4) Retirar una agrupacion musical o DJ")
print ("5) Salir\n")

while (opcion !=5):
    opcion =int(input("Digita una opcion: "))

    if opcion==1:
        print("\nEstas en la opcion 1")
    elif opcion==2:
        print("\nEstas en la opcion 2")
    elif opcion==3:
        print("\nEstas en la opcion 3")
    elif opcion==4:
        print("\nEstas en la opcion 4")
    elif opcion>5:
        print("\nopcion invalida\n")
    else: pass

print ("\n************************************\n")
print ("Saliste")
print ("\n************************************\n")