Contiene las funciones utilizadas por el programa:

stock()
compra()

Estas funciones permiten organizar el código y evitar repetir instrucciones.
El programa utiliza una lista para almacenar los productos disponibles:

lista_productos = ["repuesto1","repuesto2","repuesto3","repuesto4","repuesto5"]

El usuario solamente puede seleccionar uno de los productos que aparecen en esta lista.
El programa solicita al usuario la cantidad de productos que desea comprar.

Se utiliza try y except para evitar que el programa se cierre cuando el usuario introduce letras u otro dato que no sea un número.

while True:
    try:
        buy = int(input("Ingrese la cantidad a comprar: "))

        if buy > 0:
            break
        else:
            print("Ingrese un número mayor que 0.")

    except ValueError:
        print("Entrada no válida. Ingrese un número.")

Por ejemplo, si el usuario introduce:

Ingrese la cantidad a comprar: hola
Entrada no válida. Ingrese un número.
El programa vuelve a solicitar la cantidad.

También evita que el usuario introduzca 0 o números negativos.
Para comprobar que el producto exista, se utiliza un ciclo while:

while tipo not in lista_productos:
    print("Producto no encontrado.")

    tipo = input(
        "Ingrese repuesto1, repuesto2, repuesto3, repuesto4 o repuesto5: "
    ).lower()

El programa seguirá solicitando el producto hasta que el usuario introduzca uno válido.
Se utiliza:

.lower()

para convertir el texto ingresado a minúsculas.

Esto permite que el usuario pueda escribir:

repuesto1
REPUESTO1
Repuesto1
RePuEsTo1

y todos sean reconocidos como:

repuesto1
La función stock() permite comprobar el estado del inventario.

def stock(producto, stock_act, stock_min):
    print("Producto:", producto)
    print("Stock actual:", stock_act)
    print("Stock mínimo:", stock_min)

    if stock_act <= stock_min:
        print("Stock bajo")
    else:
        print("Stock suficiente")
        La función compra() se encarga de realizar la compra y actualizar el inventario.

def compra(producto, cantidad, stock_act):
    if cantidad <= stock_act:
        print("Compra realizada")
        stock_act -= cantidad
        return stock_act
    else:
        print("Stock insuficiente")
        return stock_act

Primero verifica si existe suficiente inventario:

if cantidad <= stock_act:

Si hay suficientes productos, resta la cantidad comprada:

stock_act -= cantidad

Después devuelve el nuevo valor del stock:

return stock_act
Si el usuario intenta comprar una cantidad superior al stock disponible, muestra: 
Stock insuficiente y mantiene el stock sin cambios.

Autor: Pedro Reyes
