
    elif opcion==2:
        #Curso de Manejo
        print("Ha ingresado al curso de manejo. \n El costo por hora varía, si desea usar un vehículo proporcionado por la academia, el costo es de 4000 colones. \n De lo contrario, el costo es de 3000 colones vehículo propio.")
        print("Tenemos un horario desde las horas 8 hasta las 17 horas.")
        cantidadHoras=float(input("¿Cuántas horas desea matricular?: "))

        if cantidadHoras>=1:

            horaDeInicio=int(input("Ingrese la hora de inicio (note que se usa formato 24 horas): "))    

            if horaDeInicio>=8 and horaDeInicio<=17:
                
                print("Ingrese el tipo de vehículo. \n 1. Vehiculo propio \n 2. Vehiculo proveído por la academia")
                tipoVehiculo=int(input("Tipo de vehiculo:"))

                if tipoVehiculo == 1:
                    costoClase=cantidadHoras*3000
                    dineroRecolectado += costoClase
                elif tipoVehiculo==2:
                    costoClase=cantidadHoras*4000
                    dineroRecolectado += costoClase
                print("El costo de la clase seria de","{:.0f}".format(costoClase),"colones.")

            else:
                print("Lo siento, la academia opera unicamente de las 8 horas hasta las 17 horas.")     

        else:
            print("Lo sentimos, no es posible matricular menos de 1 hora.")
        cantidadReservas +=1
        
