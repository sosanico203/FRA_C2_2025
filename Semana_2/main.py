import funciones

print("Bienvenidos/as al programa")

nombre = input("Ingresar nombre: ")
funciones.saludar(nombre)

numero_1 = int(input("Numero 1: "))
numero_2 = int(input("Numero 2: "))
numero_3 = int(input("Numero 3: "))

resultado_promedio = funciones.promedio(numero_1, numero_2, numero_3)

print(f"El promedio es: {resultado_promedio}")

resultado_suma, resultado_resta, resultado_multiplicacion = funciones.operar(numero_1, numero_2)

funciones.dividir(numero_1, numero_2)


base = float(input('Base del triangulo: '))
altura = float(input('Altura del triangulo: '))
funciones.area_triangulo(base, altura)

numero_4 = int(input('Nuemero 1: '))
numero_5 = int(input('Nuemero 2: '))
numero_6 = int(input('Nuemero 3: '))
funciones.buscar_mayor(numero_4, numero_5, numero_6)

numero_7 = int(input('Numero 1: '))
if funciones.es_par(numero_7):
    print('el numero es par')
else:
    print('el numero no es par')


minutos = int(input('ingrese la hora: '))
funciones.convertir_minuto(minutos)

edad = int(input('Escribe tu edad: '))
if funciones.verificar_acceso(edad):
    print('sos mayor')
else:
    print ('sos menor')

año_nacimiento = int(input('año que naciste: '))
funciones.calcular_edad(año_nacimiento)

