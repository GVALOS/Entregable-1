def stock(producto, stock_act, stock_min):
    print("producto:", producto)
    print("stock_act:", stock_act)
    print("stock_min:", stock_min)

    if stock_act <= stock_min:
        print("Stock bajo")
    else:
        print("stock suficiente")

def compra(producto, cantidad, stock_act):
    if cantidad <= stock_act:
        print("compra realizada")
        stock_act -= cantidad
    return stock_act

lista_productos = ["repuesto1", "repuesto2", "repuesto3", "repuesto4", "naranja"]
buy = int(input("Ingrese la cantidad a comprar: "))
tipo = input("Ingrese repuesto1, repuesto2, repuesto3 o repuesto4: ")

if tipo in lista_productos:
    stock_act = compra(tipo, buy, 20)
    stock(tipo, stock_act, 10)
else:
    print("Producto no encontrado")

print("cantidad comprada:", buy)