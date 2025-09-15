def mostrar_atracciones():
    print ('''Contamos con 3 atracciones 
Montaña Rusa 
Carrucel 
Casa del Terror''')

def puede_subir(edad, atraccion):
    if edad < 6:
        if atraccion == 'Carrucel':
            print ('Si puede')
        else:
            print('No puede')
    elif edad <12 and edad >= 6:
        if atraccion == 'Montaña Rusa':
            print('No puede')
        else:
            print('Si puede')
    else:
        print('Si puede')

def calcular_precio(atraccion):
    if atraccion == 'Montaña Rusa':
        precio = 1500
    elif atraccion == 'Casa del Terror':
        precio = 1200
    elif atraccion == 'Carrucel':
        precio = 800
    print(f'El precio de la atraccion es de {precio}')
    
def registrar_visita ():
    input('Ingrese su Nombre: ')
    montaña_rusa = input('¿Querés subir a la Montaña Rusa? ')
    if montaña_rusa == 'si':
        print('algo')