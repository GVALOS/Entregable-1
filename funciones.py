def stock(producto, stock_act, stock_min):
    print("\n--- INFORMACIÓN DEL STOCK ---")
    print("Producto:", producto)
    print("Stock actual:", stock_act)
    print("Stock mínimo:", stock_min)

    if stock_act <= stock_min:
        print("Stock bajo")
    else:
        print("Stock suficiente")


def compra(producto, cantidad, stock_act):
    if cantidad <= stock_act:
        print("Compra realizada")
        stock_act -= cantidad
        return stock_act, True
    else:
        print("Stock insuficiente")
        return stock_act, False


def registrar_producto(lista_productos, stocks, precios):
    nombre = input("Nombre del nuevo producto: ").strip().lower()

    if nombre == "":
        print("El nombre del producto no puede estar vacío.")
        return

    if nombre in lista_productos:
        print("Ese producto ya existe.")
        return

    while True:
        try:
            cantidad_inicial = int(input("Stock inicial: "))

            if cantidad_inicial < 0:
                print("El stock no puede ser negativo.")
            else:
                break

        except ValueError:
            print("Error: debes ingresar un número entero.")

    while True:
        try:
            precio = float(input("Precio de costo del producto: $"))

            if precio <= 0:
                print("El precio debe ser mayor que cero.")
            else:
                break

        except ValueError:
            print("Error: debes ingresar un número válido.")

    lista_productos.append(nombre)
    stocks[nombre] = cantidad_inicial
    precios[nombre] = precio

    print(f"Producto '{nombre}' registrado correctamente.")
    print(f"Stock inicial: {cantidad_inicial}")
    print(f"Precio de costo: ${precio:.2f}")


def comprar(lista_productos, stocks, compras):
    if len(lista_productos) == 0:
        print("No hay productos registrados.")
        return

    print("\nProductos disponibles:")
    print(", ".join(lista_productos))

    tipo = input("Ingrese el producto a comprar: ").strip().lower()

    if tipo not in lista_productos:
        print("Producto no encontrado.")
        return

    while True:
        try:
            buy = int(input("Ingrese la cantidad a comprar: "))

            if buy <= 0:
                print("La cantidad debe ser mayor que cero.")
            else:
                break

        except ValueError:
            print("Error: debes ingresar un número entero.")

    nuevo_stock, exito = compra(tipo, buy, stocks[tipo])

    if exito:
        stocks[tipo] = nuevo_stock
        stock(tipo, nuevo_stock, 10)
        compras.append((tipo, buy))

        print("Cantidad comprada:", buy)
        print("Nuevo stock:", nuevo_stock)


def calcular_costos_restock(stocks, precios, stock_minimo=10, margen_flete=0.05):
    print("\n" + "=" * 50)
    print("       REPORTE DE COSTOS DE RESTOCK")
    print("=" * 50)

    costo_subtotal_global = 0.0
    se_requiere_restock = False

    for producto, cantidad_actual in stocks.items():
        precio_costo = precios.get(producto, 0.0)

        if cantidad_actual <= stock_minimo:
            se_requiere_restock = True

            meta_inventario = stock_minimo * 2
            cantidad_a_pedir = meta_inventario - cantidad_actual
            costo_subtotal = cantidad_a_pedir * precio_costo
            costo_subtotal_global += costo_subtotal

            stocks[producto] += cantidad_a_pedir

            print(f"\nProducto: {producto.upper()}")
            print(f" > Stock actual: {cantidad_actual} | Mínimo: {stock_minimo}")
            print(f" > Piezas a reponer: {cantidad_a_pedir}")
            print(f" > Costo unitario: ${precio_costo:.2f}")
            print(f" > Subtotal restock: ${costo_subtotal:.2f}")
            print("-" * 50)

    if not se_requiere_restock:
        print("\nTodos los productos tienen suficiente stock.")
        print("No se requiere inversión de restock.")
        return 0.0, 0.0

    costo_total_flete = costo_subtotal_global * margen_flete
    costo_gran_total = costo_subtotal_global + costo_total_flete

    print("\n" + "=" * 50)
    print(f"SUBTOTAL NETO DE COMPRAS: ${costo_subtotal_global:.2f}")
    print(f"FLETE Y LOGÍSTICA ({int(margen_flete * 100)}%): ${costo_total_flete:.2f}")
    print(f"COSTO TOTAL ESTIMADO: ${costo_gran_total:.2f}")
    print("=" * 50)

    return costo_subtotal_global, costo_gran_total


def mostrar_productos(lista_productos, stocks, precios):
    print("\n--- LISTA DE PRODUCTOS ---")

    if len(lista_productos) == 0:
        print("No hay productos registrados.")
        return

    for producto in lista_productos:
        print(f"Producto: {producto} | Stock: {stocks[producto]} | Precio: ${precios[producto]:.2f}")


def mostrar_compras(compras):
    print("\n--- COMPRAS REALIZADAS ---")

    if len(compras) == 0:
        print("No se han realizado compras.")
        return

    for producto, cantidad in compras:
        print(f"Producto: {producto} | Cantidad comprada: {cantidad}")


def user(lista_productos, stocks, compras, precios):
    while True:
        print("\n" + "=" * 50)
        print("           SELECCIÓN DE USUARIO")
        print("=" * 50)
        print("Si es un usuario, ingrese 1")
        print("Si es un administrador, ingrese 2")
        print("Si gusta retirarse, ingrese 3")

        try:
            rol = int(input("Ingrese: "))

        except ValueError:
            print("Opción inválida")
            continue

        if rol == 1:
            while True:
                print("\n")
                print("=" * 50)
                print("             TIENDA")
                print("=" * 50)
                print("1. Comprar producto")
                print("2. Ver lista de productos")
                print("3. Regresar")
                print("=" * 50)

                try:
                    opcion = int(input("Elija una opción: "))

                except ValueError:
                    print("Error: debes ingresar un número del 1 al 3.")
                    continue

                if opcion == 1:
                    comprar(lista_productos, stocks, compras)

                elif opcion == 2:
                    mostrar_productos(lista_productos, stocks, precios)

                elif opcion == 3:
                    print("Regresando al menú principal...")
                    break

                else:
                    print("Opción inválida. Debes elegir entre 1 y 3.")

        elif rol == 2:
            us = "admin"
            cont = "1234"

            usuario = input("Usuario de administrador: ").strip()
            contra = input("Contraseña: ").strip()

            if us != usuario or cont != contra:
                print("Credenciales incorrectas.")
                continue

            while True:
                print("\n")
                print("=" * 50)
                print("             SISTEMA DE INVENTARIO")
                print("=" * 50)
                print("1. Registrar producto")
                print("2. Comprar producto")
                print("3. Ver lista de productos")
                print("4. Ver compras realizadas")
                print("5. Ver costos de restock")
                print("6. Regresar")
                print("=" * 50)

                try:
                    opcion = int(input("Elija una opción: "))

                except ValueError:
                    print("Error: debes ingresar un número del 1 al 6.")
                    continue

                if opcion == 1:
                    registrar_producto(lista_productos, stocks, precios)

                elif opcion == 2:
                    comprar(lista_productos, stocks, compras)

                elif opcion == 3:
                    mostrar_productos(lista_productos, stocks, precios)

                elif opcion == 4:
                    mostrar_compras(compras)

                elif opcion == 5:
                    calcular_costos_restock(stocks, precios)

                elif opcion == 6:
                    print("Regresando al menú principal...")
                    break

                else:
                    print("Opción inválida. Debes elegir entre 1 y 6.")

        elif rol == 3:
            print("Saliendo del sistema...")
            return

        else:
            print("Opción inválida.")