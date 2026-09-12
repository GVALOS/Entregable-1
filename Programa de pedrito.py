def stock(producto, stock_act, stock_min): #definimos la funcion stock
    print("producto:", producto) #hacemos la impresión de la variable producto
    print("stock_act:", stock_act) #hacemos la impresión de la variable stock_act
    print("stock_min:", stock_min) #hacemos la impresión de la variable stock_min

    if stock_act <= stock_min: #verificamos si el stock actual es menor o igual al stock mínimo
        print("Stock bajo")
    else:
        print("stock suficiente")

def compra(producto, cantidad, stock_act): #definimos la funcion compra
    if cantidad <= stock_act:
        print("compra realizada") #hacemos la impresión de que la compra fue realizada
        stock_act -= cantidad
    return stock_act
#  definimos la lista de productos disponibles y solicitamos al usuario la cantidad a comprar y el tipo de repuesto que desea adquirir
lista_productos = ["repuesto1", "repuesto2", "repuesto3", "repuesto4", "repuesto5"]
buy = int(input("Ingrese la cantidad a comprar: "))
tipo = input("Ingrese repuesto1, repuesto2, repuesto3, repuesto4 o repuesto5: ")

if tipo in lista_productos: #verificamos si el tipo de repuesto ingresado por el usuario se encuentra en la lista de productos disponibles
    stock_act = compra(tipo, buy, 20)
    stock(tipo, stock_act, 10)
    print("cantidad comprada:", buy)
else:
    print("Producto no encontrado") #hacemos la impresión de que el producto no fue encontrado
