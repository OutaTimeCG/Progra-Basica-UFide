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

print("Bienvenido! Ingrese el numero correspodiente al servicio que desea: \n 1. Curso Teórico \n 2. Curso de Manejo \n 3. Dictamen Médico.")
opcion = int(input("Seleccione una opcion:"))


if opcion==1:
    #Curso Teorico
    print("Ha ingresado al curso teorico. \n El costo por hora es de 2000 colones.")
    cantidadHoras=float(input("¿Cuántas horas desea matricular?: "))
    horaDeInicio=int(input("Ingrese la hora de inicio (note que se usa formato 24 horas): "))    

    if horaDeInicio>=8 and horaDeInicio<=21:
        costoClase=cantidadHoras*2000
        print("El costo de la clase seria de",costoClase,"colones.")
    else:
        print("Lo siento, la academia opera unicamente de las 8 horas hasta las 21 horas.")     

elif opcion==2:
    #Curso de Manejo
    print("Ha ingresado al curso de manejo. \n El costo por hora varía, si desea usar un vehículo proporcionado por la academia, el costo es de 4000 colones. \n De lo contrario, el costo es de 3000 colones vehículo propio.")
    cantidadHoras=float(input("¿Cuántas horas desea matricular?: "))

    horaDeInicio=int(input("Ingrese la hora de inicio (note que se usa formato 24 horas): "))    

    if horaDeInicio>=8 and horaDeInicio<=17:
        
        print("Ingrese el tipo de vehículo. \n 1. Vehiculo propio \n 2. Vehiculo proveído por la academia")
        tipoVehiculo=int(input("Tipo de vehiculo:"))

        if tipoVehiculo == 1:
            costoClase=cantidadHoras*3000
        elif tipoVehiculo==2:
            costoClase=cantidadHoras*4000
        print("El costo de la clase seria de",costoClase,"colones.")

    else:
        print("Lo siento, la academia opera unicamente de las 8 horas hasta las 17 horas.")     

#elif opcion ==3:
    
#else:
#print("Lo sentimos, el numero que marco es incorrecto")