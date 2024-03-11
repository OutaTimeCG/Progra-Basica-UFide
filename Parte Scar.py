    elif opcion==3:
        #Dictamen
        #tipo sangre, peso, estatura y si desea ser donador.
        print("Proceso del dictamen medico:")
        tipoSangre=input("Ingrese su tipo de sangre: ")
        peso=input("Ingrese su peso en kg: ")
        estatura=input("Ingrese su estatura en cm: ")
        donador=input("¿Desea ser donador? (Ingresar Si/No)") 

        print("Dictamen medico de la persona:")
        print("Nombre:",nombre)
        print("Numero:",telefono)
        print("Correo Electronico:",correo)
        print("Tipo de sangre: ",tipoSangre)
        print("Peso en kg:",peso,"kg")
        print("Estatura en cm:",estatura,"cm")
        print("Es donador:",donador)

    elif opcion==4:
        print("Esta solicitando acceso al sistema administrador.")
        intentoContra=input("Ingrese la contraseña:")
        if intentoContra == claveAdmin:
            print("Ha ingreado al sistema de administrador.")
            funcAdmin=int(input("Ingrese el numero correspodiente al servicio que desea: \n 1. Ver la cantidad de dinero recolectado \n 2. Ver sel número de reservas"))

            if funcAdmin==-1:
                print("Cantidad de dinero recolectado:",dineroRecolectado,"colones.")
            elif funcAdmin==2:
                print("Cantidad de reservas:",cantidadReservas)
    
    print("Gracias por usar el sistema!")
    break