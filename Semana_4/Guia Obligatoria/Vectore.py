# Punto 1
# declarando un array (lista) de 5 enteros
numero = [0] * 5

# cargando los numeros por teclado
for i in range(5):
    numero[i] = int(input(f'ingrese un numero {i+1}: '))

# mostrar los numeros acumulados 
print("Contenido de array: ")
for i in range (5):
    print(f"Posicion {i}: {numero[i]}")

# Punto 2
# declarando un array (lista) de 10 enteros  
numeros = [0] * 10

# cargando los numeros por teclado
for i in range (10):
    numeros[i] = int(input(f"ingrese un numero {i+1} : "))

# sumar todos los numeros ingresados 
suma = 0
for i in range(10):
    suma += numeros[i]

# mostrar el resultado de la suma de los numeros 
print(f"la suma de todos los numeros es de: ", suma)

# Punto 3
# declarando array de 6 numeros flotantes (float)
numeros_float = [0.0] *6

# cargando los numeros por teclado
for i in range (6):
    numeros_float[i] = float(input(f"Ingrese numeros flotantes {i+1}: "))

# calculando el promedio
suma = 0
for i in range (6):
    suma += numeros[i]

promedio = suma /6

# mostrando el promedio
print("el promedio de los numeros es de: ", promedio)

# Punto 4
# declarando un array de 8 numeros enteros (int)
numeros_4 = [0] * 8

# cargando los numeros por teclado 
for i in range(8):
    numeros_4 [i] = int(input(f"Ingrese los numeros {i+1}: "))

# contando cuantos son mayores a 100
contador = 0
for i in range(8):
    if numeros_4[i] > 100:
        contador += 1

# mostrando resultados 
print("Cantidad de numeros mayor a 100: ", contador)


#Punto 5
# array de 10 enteros
numeros_5 = [0] *10

# cargando numeros por teclado
for i in range(10):
    numeros_5[i] = int(input(f"Ingrese un numero {i+1}: "))

# pedir el numero que se quiere buscar 
buscar = int(input("ingrese el numero que desea buscar: "))

# verificando si se encuentra en el array 
encontrado = False
for i in range (10):
    if numeros_5[i] == buscar:
        print(f"El numero {buscar} se encuntra en la posicion {i} ")
        encontrado = True 
        break

if not encontrado:
    print (f"El numero {buscar} No se encuentra en el array ")

# Punto 6
# declarando array de 7 numeros enteros 
numeros_6 = [0] * 7

# cargardo numeros por teclado 
for i in range(7):
    numeros_6[i] = int(input(f"Ingrese un numero {i+1}: "))

# iniciando maximo con el primer valor
maximo = numeros_6[i]
posicion = 0

# buscando el valor mas alto y su pocision 
for i in range (1, 7):
    if numeros_6[i] > maximo:
        maximo = numeros_6[i]
        posicion = i

#mostrando resultado 
print(f"El valor mas alto es {maximo} y se encuentra en la posicion {posicion}")

# Punto 7
# array de 6 numeros enteros (int)
numeros_7 =[0] *6

#cargando numeros por teclado
for i in range(6):
    numeros_7[i] = int(input(f"Ingrese sus numeros {i+1}: "))

# mostrando el array invertido
print("lista invertida: ")
for i in range(5 -1 -1):
    print(numeros_7[i])

# Punto 8
# declarando dos arrays de 5 numeros enteros (int)
array1 = [0] *5
array2 = [0] *5

#cargnado el primer array
print("cargando el primer array:")
for i in range(5):
    array1[i] = int(input(f"ingrese un numero {i+1}: "))

#cargnado el segundo array
print("cargando el primer array:")
for i in range(5):
    array2[i] = int(input(f"ingrese un numero {i+1}: "))

#comparando los elementos 
iguales = True
for i in range (5):
    if array1[i] != array2[i]:
        iguales = False
        break

if iguales:
    print("los arrays son iguales")
else:
    print("los arrays no son iguales")

# Punto 9
# declarando array de 10 numeros enteros (int)
numeros_9 = [0] *10

for i in range (10):
    numeros_9[i] = int(input(f"ingrese un numero {i+1}: "))

# reempalaza los numeros pares por 0 
for i in range(10):
    if numeros_9[i] % 2 == 0:
        numeros_9[i] = 0

print("array de los elementos: ")
for num in numeros_9:
    print(num)

# Punto 10
def buscar_numero(array, numero_10):
    for i in range(6):
        if array[i] == numero_10:
            return 1
    return -1

numeros10 = [4, 5, 8, 3, 7, 9]
buscar_numero10 = int(input("Ingrese un numero "))
posicion10 = buscar_numero (numero, buscar)

if posicion10 != -1:
    print (f"el numero {buscar_numero10} se encuentra en la posicion {posicion10}")
else:
    print(f"el numero {buscar_numero10} no se encuentra en el array")