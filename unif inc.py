def stock(producto, stock_act, stock_min):
    print("producto:", producto)
    print("Stock actual:", stock_act)
    print("Stock minimo:", stock_min)

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


def registrar_producto(lista_productos, stocks):
    nombre = input("Nombre del nuevo producto: ").strip().lower()

    if nombre in lista_productos:
        print("Ese producto ya existe.")
        return

    cantidad_inicial = int(input("Stock inicial: "))

    lista_productos.append(nombre)
    stocks[nombre] = cantidad_inicial

    print(f"Producto '{nombre}' registrado con stock {cantidad_inicial}")


def comprar(lista_productos, stocks, compras):
    print("Productos disponibles:", ", ".join(lista_productos))

    tipo = input("Ingrese el producto a comprar: ").strip().lower()

    if tipo not in lista_productos:
        print("Producto no encontrado")
        return

    buy = int(input("Ingrese la cantidad a comprar: "))

    nuevo_stock, exito = compra(tipo, buy, stocks[tipo])

    stocks[tipo] = nuevo_stock

    stock(tipo, nuevo_stock, 10)

    if exito:
        compras.append((tipo, buy))
        print("Cantidad comprada:", buy)


def calcular_costos_restock (stocks, precios, stock_minimo=10, margen_flete=0.05):

    print("/" + "="*50)
    print(" REPORTE DE COSTOS DE RESTOCK")
    print("="*50)

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

    print(f"Producto: {producto.upper()}")
    print(f" > Stock actual: {cantidad_actual}| Minimo: {stock_minimo}")
    print(f" > Piezas a reponer: {cantidad_a_pedir} unidades")
    print(f" > Costo unitario: ${precio_costo:.2f}")
    print(f" > Subtotal restock: ${costo_subtotal:.2f}")
    print("-"*50)

    if not se_requiere_restock:
        print("Todos los productos tienen suficiente stock. No se requiere inversion de restock.")
        return 0.0, 0.0

    costo_total_flete = costo_subtotal_global * margen_flete
    costo_gran_total = costo_subtotal_global + costo_total_flete

    print(f"SUBTOTAL NETO DE COMPRAS: ${costo_subtotal_global:.2f}")
    print(f"FLETE Y LOGISTICA ({int(margen_flete*100)}%): ${costo_total_flete:.2f}")
    print(f"COSTO TOTAL ESTIMADO RESTOCK: ${costo_gran_total:.2f}")
    print("="*50 + "/n")

    return costo_subtotal_global, costo_gran_total



lista_productos = [
    "repuesto1",
    "repuesto2",
    "repuesto3",
    "repuesto4"
]

stocks = {
    "repuesto1": 20,
    "repuesto2": 20,
    "repuesto3": 20,
    "repuesto4": 20
}

compras = []


while True:
    print("\n MENÚ ")
    print("1. Registrar producto")
    print("2. Comprar producto")
    print("3. Ver lista de productos")
    print("4. Ver compras realizadas")
    print("5. Salir")

    opcion = input("Elija una opción: ").strip()

    if opcion == "1":
        registrar_producto(lista_productos, stocks)

    elif opcion == "2":
        comprar(lista_productos, stocks, compras)

    elif opcion == "3":
        print(lista_productos)

    elif opcion == "4":
        print(compras)

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")