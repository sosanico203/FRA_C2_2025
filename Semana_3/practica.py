#realizar un pequeño sistema de gestion en consola para que una concecionaria
#puedacargar ventas, la misma se detiene cuando se ingrresa 0. El programa debe informar al final:
#          1.  La venta mayor
#          2.  La venta menor
#          3.  Cantidad de ventas realizadas
#          4.  El total de ventas

total_ventas = 0 #acumulador (incrementar por monto de venta)
cantidad_ventas = 0 #contasdor (incrementa de a uno)

venta_mayor = None #Se va a guardar la venta de mayor monto
venta_menor = None #Se va a guardar la venta de menor monto

while True:
    # (ENTRADA) ingreso de ventas 
    venta = float(input('Ingresar venta (Para finalizar ingresar 0): '))
    # Corte de ciclo
    if venta == 0:
        break
    # (Procesos) acumulamos ventas y contamos ventas
    total_ventas += venta
    cantidad_ventas += 1

    #(PROCESO) Buscmaos mayor y menor

    if cantidad_ventas == 1: #Condicional que incia debase nuestras  
        venta_mayor = venta
        venta_menor = venta
    else:
        # Condicional interno que compara mayores
        if venta > venta_mayor:
        # Segundo condicional interno que compara menores
            venta_mayor = venta
        if venta < venta_menor:
            venta_menor = venta
    # (PROCESO) calculamos promedio de ventas 
    promedio_ventas = total_ventas / cantidad_ventas

    #(SALIDA) se muestran los valores
    print(f'Total de ventas realizadas{cantidad_ventas} con un monto de: {total_ventas}')

    # Validacion de existencias de ventas para mostrar se mayor, menor y promdedio de ventas
    if cantidad_ventas > 0:
        print(f'Venta mayor {venta_mayor}')
        print(f'Venta menor {venta_menor}')
        print(f'El promedio de ventas es: {promedio_ventas}')
    else:
        print('No se registraron ventas mayores o menores...')