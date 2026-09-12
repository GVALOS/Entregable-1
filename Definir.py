def stock(producto, stock_act, stock_min):
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
        return stock_act
    else:
        print("Stock insuficiente")
        return stock_act


