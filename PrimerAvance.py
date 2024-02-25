# Universidad Fidélitas.
# Proyecto de programación basica.
# Curso: SC-202, Programacion basica (Introducción a la programación). 
# Tema del proyecto: Academia de manejo.
# Grupo #2
# Integrantes: Jose Castro. Juan Castro. Luna Castillo. Scarlet Villamizar.

print("Este es el sistema de la academia de manejo Fidélitas.")

#Entradas
nombre=input("Ingrese su nombre: ")
telefono=input("Ingrese su número de teléfono, sin espacios, ni guiones: ")
correo=input("Ingrese su dirección de correo electrónico: ")

#Definicion de variables
claveAdmin = "4Dm1N123"
dineroRecolectado = 0
cantidadReservas = 0


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