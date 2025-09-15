altura = float(input('Ingrese su altura: '))

if altura <= 1.60:
    print('Tu posicion de juego es Base')
elif altura >= 1.60 and altura <= 1.79:
    print('Tu posicion es de Escolta')
elif altura >= 1.80 and altura < 2.0:
    print('Tu posicion es de Alero')
else:
    altura >= 2.0
    print ('Tu posicion es de Pivot')