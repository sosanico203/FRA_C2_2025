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
    elif edad < 12 and edad >= 6:
        if atraccion == 'Montaña Rusa':
            print('No puede')
        else:
            print('Si puede')

def calcular_precio(atraccion):
    