from Definir import stock, compra

# Lista de productos disponibles
lista_productos = ["repuesto1", "repuesto2", "repuesto3", "repuesto4", "repuesto5"]
# Stock actual
stock_act = 20
# Stock mínimo
stock_min = 10
# Pedimos la cantidad que desea comprar
# El programa seguirá preguntando hasta recibir un número válido
while True:
    try:
        buy = int(input("Ingrese la cantidad a comprar: "))

        # Verificamos que la cantidad sea mayor que cero
        if buy > 0:
            break
        else:
            print("Ingrese un número mayor que 0.")

    # Si el usuario escribe letras o algo que no se pueda convertir
    # a entero, mostramos un mensaje y volvemos a preguntar
    except ValueError:
        print("Entrada no válida. Ingrese un número.")


# Pedimos el tipo de producto
tipo = input(
    "Ingrese repuesto1, repuesto2, repuesto3, repuesto4 o repuesto5: "
).lower()


# Verificamos que el producto exista
while tipo not in lista_productos:
    print("Producto no encontrado.")

    tipo = input(
        "Ingrese repuesto1, repuesto2, repuesto3, repuesto4 o repuesto5: "
    ).lower()


# Realizamos la compra y actualizamos el stock
stock_act = compra(tipo, buy, stock_act)

# Comprobamos el estado del stock
stock(tipo, stock_act, stock_min)

# Mostramos la cantidad comprada
print("Cantidad comprada:", buy)