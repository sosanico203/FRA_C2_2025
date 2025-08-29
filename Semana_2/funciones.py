def saludar(nombre: str)->None:
    print(f"Hola {nombre}")
    
def promedio(a:int, b:int, c:int)-> float:
    #resultado = (a + b + c) /3
    #return resultado
    return (a + b + c) /3

def operar(a:int, b: int)->int:
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    return suma, resta, multiplicacion

def dividir(a:int, b: int)->None:
    print(f"La división es: {a / b}")

def area_triangulo(a:float, b:float):
    area = (a * b) / 2
    print(f'El area del triangulo es {area}')

def buscar_mayor(a:int, b:int, c:int):
    if a > b and a > c:
        if b > c:
            return print(a, b, c)
        else:
            return print(a, c, b)
    elif b > a and b > c:
        if a > c:
            return print(b, a, c)
        else:
            return print(b, c, a)
    else: 
        if a > b:
            return print(c, a, b)
        else:
            return print(c, b , a)
        
def es_par(a:int):
    if a % 2 == 0:
        return True 
    else:
        return False
    

def convertir_minuto(a:int):
    horas = a // 60
    minutos_sobrantes = a % 60
    return print( f'son {horas} horas, y {minutos_sobrantes} minutos')


def verificar_acceso(a:int):
    if a >= 18:
        return True
    else:
        return False
    

def calcular_edad(a:int):
    edad = 2025 - a
    print(f'tu edad es {edad}')