# ===================================
# GESTIÓN DE BIBLIOTECA
# ===================================

MAX_TITULOS = 20
titulos = [""] * MAX_TITULOS       # Lista de títulos (vacía al inicio)
ejemplares = [0] * MAX_TITULOS     # Lista de ejemplares
cantidad_titulos = 0               # Contador real de libros cargados


# -------------------------------
# 1. Cargar títulos y ejemplares
# -------------------------------
def cargar_titulos():
    global cantidad_titulos
    while cantidad_titulos < MAX_TITULOS:
        titulo = input("Ingrese el título (o 'fin' para terminar): ")
        if titulo.lower() == "fin":
            break

        # Verificar si ya existe
        existe = False
        for i in range(cantidad_titulos):
            if titulos[i] == titulo:
                existe = True
                break
        if existe:
            print("Ese título ya está cargado.")
            continue

        copias = int(input(f"Ingrese cantidad de ejemplares para '{titulo}': "))
        titulos[cantidad_titulos] = titulo
        ejemplares[cantidad_titulos] = copias
        cantidad_titulos += 1


# -------------------------------
# 2. Mostrar catálogo completo
# -------------------------------
def mostrar_catalogo():
    if cantidad_titulos == 0:
        print("Catálogo vacío.")
    else:
        print("\n--- Catálogo de Libros ---")
        for i in range(cantidad_titulos):
            print(f"{titulos[i]} → {ejemplares[i]} copias")


# -------------------------------
# 3. Consultar disponibilidad
# -------------------------------
def consultar_disponibilidad():
    titulo = input("Ingrese el título a consultar: ")
    for i in range(cantidad_titulos):
        if titulos[i] == titulo:
            print(f"{titulo} tiene {ejemplares[i]} copias disponibles")
            return
    print("Ese título no está en el catálogo.")


# -------------------------------
# 4. Listar títulos agotados
# -------------------------------
def listar_agotados():
    hay_agotados = False
    for i in range(cantidad_titulos):
        if ejemplares[i] == 0:
            if not hay_agotados:
                print("\nTítulos agotados:")
                hay_agotados = True
            print(f"- {titulos[i]}")
    if not hay_agotados:
        print("No hay títulos agotados.")


# -------------------------------
# 5. Agregar un nuevo título
# -------------------------------
def agregar_titulo():
    global cantidad_titulos
    if cantidad_titulos >= MAX_TITULOS:
        print("No se pueden agregar más títulos (máximo alcanzado).")
        return

    titulo = input("Ingrese el nuevo título: ")

    # Verificar si ya existe
    for i in range(cantidad_titulos):
        if titulos[i] == titulo:
            print("Ese título ya existe.")
            return

    copias = int(input(f"Ingrese cantidad de ejemplares para '{titulo}': "))
    titulos[cantidad_titulos] = titulo
    ejemplares[cantidad_titulos] = copias
    cantidad_titulos += 1
    print(f"Título '{titulo}' agregado con {copias} ejemplares.")


# -------------------------------
# 6. Actualizar ejemplares
# -------------------------------
def actualizar_ejemplares():
    titulo = input("Ingrese el título a actualizar: ")
    for i in range(cantidad_titulos):
        if titulos[i] == titulo:
            print(f"Ejemplares actuales de '{titulo}': {ejemplares[i]}")
            opcion = input("¿Préstamo (P) o Devolución (D)? ").upper()

            if opcion == "P":
                if ejemplares[i] > 0:
                    ejemplares[i] -= 1
                    print(f"Préstamo registrado. Quedan {ejemplares[i]} copias de '{titulo}'.")
                else:
                    print("No hay ejemplares disponibles para préstamo.")
            elif opcion == "D":
                ejemplares[i] += 1
                print(f"Devolución registrada. Ahora hay {ejemplares[i]} copias de '{titulo}'.")
            else:
                print("Opción inválida.")
            return
    print("Ese título no está en el catálogo.")


# -------------------------------
# 7. Menú principal
# -------------------------------
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Cargar títulos y ejemplares")
        print("2. Mostrar catálogo completo")
        print("3. Consultar disponibilidad")
        print("4. Listar títulos agotados")
        print("5. Agregar un nuevo título")
        print("6. Actualizar ejemplares (préstamo / devolución)")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_titulos()
        elif opcion == "2":
            mostrar_catalogo()
        elif opcion == "3":
            consultar_disponibilidad()
        elif opcion == "4":
            listar_agotados()
        elif opcion == "5":
            agregar_titulo()
        elif opcion == "6":
            actualizar_ejemplares()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")


# -------------------------------
# Ejecución del programa
# -------------------------------
menu()
