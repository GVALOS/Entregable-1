# Importamos las funciones "stock" y "compra" desde el archivo Definir.py
from Definir import stock, compra

# Creamos una lista que contiene todos los productos disponibles
lista_productos = ["repuesto1", "repuesto2", "repuesto3", "repuesto4", "repuesto5"]

# Definimos la cantidad actual de productos disponibles en el inventario
stock_act = 20

# Definimos la cantidad mínima de productos que debe haber en el inventario
stock_min = 10

# Le pedimos al usuario que ingrese la cantidad de productos que desea comprar
# int() convierte el dato ingresado de texto a un número entero
buy = int(input("Ingrese la cantidad a comprar: "))

# Le pedimos al usuario que ingrese el nombre del repuesto que desea comprar
# .lower() convierte todo lo escrito a minúsculas
# Esto permite aceptar entradas como REPUESTO1, Repuesto1 o repuesto1
tipo = input("Ingrese repuesto1, repuesto2, repuesto3, repuesto4 o repuesto5: ").lower()

# Comprobamos si el producto ingresado NO se encuentra en la lista
# Mientras el producto no sea válido, el programa seguirá preguntando
while tipo not in lista_productos:

    # Mostramos un mensaje indicando que el producto ingresado no existe
    print("Producto no encontrado.")

    # Volvemos a pedir al usuario que ingrese un producto
    # .lower() permite aceptar mayúsculas y minúsculas
    tipo = input("Ingrese repuesto1, repuesto2, repuesto3, repuesto4 o repuesto5: ").lower()

# Llamamos a la función "compra"
stock_act = compra(tipo, buy, stock_act)
# Llamamos a la función "stock"
stock(tipo, stock_act, stock_min)
# Mostramos en pantalla la cantidad de productos que compró el cliente
print("Cantidad comprada:", buy)