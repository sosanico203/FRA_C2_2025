nombre = input('''¡BUENAS VISITANTE!
Coloque su nombre: ''')

edad = int(input('¿Cuántos años tenés?: '))

int(input('''Contamos con un total de 3 atracciones:
- Montaña rusa (1500)
- Casa del terror (1200)
- Carrusel (800)
¿Cuántas atracciones querés visitar?: '''))

#Precios de las atracciones
precio_montaña = 1500
precio_casa = 1200
precio_carrusel = 800

#variables para el resumen
total = 0
elegidas = ""
permitidas = ""
denegadas = ""

#que puede usar dependiendo la edad
if edad < 6:
    print('Solo podés acceder al carrusel')
elif edad < 12:
    print('Podés acceder al carrusel y a la casa del terror')
else:
    print('Podés acceder a cualquier atracción, incluida la montaña rusa')

#preguntar que atracciones quieres usar 
print("Respondé con 'si' o 'no':")

montaña_rusa = input('¿Querés subir a la Montaña Rusa? ')
if montaña_rusa == 'si':
    elegidas += "Montaña Rusa"
    if edad >= 12:
        print('Podés subir a la Montaña Rusa')
        permitidas += "Montaña Rusa"
        total += precio_montaña
    else:
        print('No podés subir a la Montaña Rusa, necesitás al menos 12 años')
        denegadas += "Montaña Rusa"

casa_terror = input('¿Querés entrar a la Casa del Terror? ')
if casa_terror == 'si':
    elegidas += "Casa del Terror"
    if edad >= 6:
        print('Podés entrar a la Casa del Terror')
        total += precio_casa
    else:
        print('No podés entrar a la Casa del Terror, necesitás al menos 6 años')
        denegadas += "Casa del Teror"

carrusel = input('¿Querés subir al Carrusel? ')
if carrusel == 'si':
    elegidas += "Carrusel"
    print('Podés subir al Carrusel (apto para todas las edades)')
    total += precio_carrusel

print("========= RESUMEN DE VISITA =========")
print(f"Visitante: {nombre}")
print(f"Edad: {edad} años")

print("Atracciones elegidas:")
print(f"{elegidas}")

print("Atracciones permitidas:")
print(f"{permitidas}")

print("Atracciones denegadas (por la edad):")
print(f"{denegadas}")

print(f" Costo total: ${total}")
print("===========================================")