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

lista_productos = ["repuesto1", "repuesto2", "repuesto3", "repuesto4"]
stocks = {"repuesto1": 20, "repuesto2": 20, "repuesto3": 20, "repuesto4": 20}
compras = []

while True:
    print(" MENÚ ")
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