while(True):
    print("Bienvenido! Ingrese el numero correspodiente al servicio que desea: \n 1. Curso Teórico \n 2. Curso de Manejo \n 3. Dictamen medico \n 4.Sistema administrador")
    opcion = int(input("Seleccione una opcion:"))
    if opcion==1:
        #Curso Teorico
        print("Ha ingresado al curso teorico. \n El costo por hora es de 2000 colones.")
        cantidadHoras=float(input("¿Cuántas horas desea matricular?: "))
        print("Tenemos un horario desde las horas 8 hasta las 21 horas.")
        horaDeInicio=int(input("Ingrese la hora de inicio (note que se usa formato 24 horas): "))    

        if horaDeInicio>=8 and horaDeInicio<=21:
            costoClase=cantidadHoras*2000
            print("El costo de la clase seria de","{:.0f}".format(costoClase),"colones.")
            dineroRecolectado += costoClase
        else:
            print("Lo siento, la academia opera unicamente de las 8 horas hasta las 21 horas.")
        cantidadReservas +=1
        

