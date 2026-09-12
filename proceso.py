from Definir import stock, compra

lista_productos = ["repuesto1", "repuesto2", "repuesto3", "repuesto4", "repuesto5"]

stock_act = 20
stock_min = 10

buy = int(input("Ingrese la cantidad a comprar: "))
tipo = input("Ingrese repuesto1, repuesto2, repuesto3, repuesto4 o repuesto5: ")

if tipo in lista_productos:
    stock_act = compra(tipo, buy, stock_act)
    
    stock(tipo, stock_act, stock_min)
    
    print("Cantidad comprada:", buy)

else:
    print("Producto no encontrado")