# Definimos la función "stock", que sirve para revisar el estado
def stock(producto, stock_act, stock_min):

    # Mostramos el nombre del producto
    print("Producto:", producto)

    # Mostramos la cantidad actual de productos disponibles
    print("Stock actual:", stock_act)

    # Mostramos cuál es la cantidad mínima de productos establecida
    print("Stock mínimo:", stock_min)

    # Comprobamos si el stock actual es menor o igual
    # al stock mínimo establecido
    if stock_act <= stock_min:

        # Si se cumple la condición, mostramos que hay poco stock
        print("Stock bajo")

    else:

        # Si no se cumple la condición, significa que
        # todavía hay suficiente cantidad de productos
        print("Stock suficiente")

# Definimos la función "compra", que se encarga de realizar
def compra(producto, cantidad, stock_act):

    # Comprobamos si la cantidad que el cliente quiere comprar
    # es menor o igual a la cantidad disponible en el stock
    if cantidad <= stock_act:
        # Si hay suficientes productos, mostramos que la compra
        print("Compra realizada")
        # Restamos la cantidad comprada al stock actual
        stock_act -= cantidad
        # Devolvemos el nuevo valor del stock
        return stock_act
    else:
        # Si el cliente intenta comprar más productos
        # de los que hay disponibles, mostramos este mensaje
        print("Stock insuficiente")
        # Devolvemos el stock sin modificarlo
        return stock_act

