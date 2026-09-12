#Sistema de Gestion de Inventario y Restock de Repuestos

##Descripcion del programa
Este programa en Python permite gestionar el inventario de una tienda de repuestos. Integra funciones para controlar el nivel de stock de los productos, realizar transacciones de compra/descuento de inventario, resgistrar nuevos repuestos y calcular de forma automatica el costo necesario para finalizar el reabastecimiento considerando fletes y logistica.

##Integrantes del Equipo y Aportes

|Pedro Reyes|Evaluacion de Inventario| Diseño la logica para evaluar la cantidad actual de productos contra el stock minimo permitido.|
|Rodrigo|Gestion de Restock y Compras| Implemento las funciones para procesar transacciones de compra, registrar nuevos productos y el menu interactivo.|
|Daniel Brizuela|Analisis Financiero de Restock| Desarolle el calculo de cosotos de reabastecimiento, subtotales por repuesto y estimacion con flete.|
|Pedro Valle|Pruebas/Aseguramiento de calidad|Encargado de realizar las pruebas de codigo y vereficar casos de borde (ej. stock insuficiente, opciones invalidas).|
|Gabriel Avalos|Revisor de Codigo y Control de github|Encargado de revisar y modificar el codigo segun las instrucciones dadas, ademas de verificar la correcta integracion del codigo y publicacion del repositorio en Github.|

##Como ejecutar el Programa

###Requisitos
#Tener instalado Python 3.12 en el sistema.

    ###Pasos para la ejecucion:
    1.Clona o descarga el repositorio que contiene el archivo "main.py" desde Github
    2.Abre la terminal o consola de comandos en la carpeta del proyecto
    3.Ejecuta el comando:
    ```bash
    python main.py.

#Documentacion de Funciones
1. stock(producto, stock_act, stock_min)

#parametros:
    producto(str): Nombre o identificador del repuesto
    stock_act(int): Cantidad actual disponible en el inventario.
    stock_min(int):Cantidad minima requerida de inventario.
#retorno:
    none

2. compra(producto, cantidad, stock_act)

#Parametros:
    producto(str): Nombre del repuesto a comprar.
    cantidad(int): Unidades que se desean comprar.
    stock_act(int): Cantidad disponible actualmente.

#Retorno:
    (tuple) (nuevo_stock, exito)
        nuevo_stock(int): Cantidad restante tras la transaccion
        exito(bool): True si la compra fue exitosa, False si el stock fue insuficiente.

3. resgistrar_producto(lista_productos, stocks)

#Parametros:
    lista_productos(list): Lista con los nombres de los productos registrados
    stocks(dict): Diccionario que asocia el nombre del producto con su cantidad disponible.

#Retorno:
    none

4. comprar(lista_productos, stocks, compras)

#Parametros:
    lista_productos(list): Productos registrados en el sistema.
    stocks(dict): Registro de inventario actual.
    compras(list): Historial donde se almacenan las compras realizadas (producto, cantidad).

#Retorno:
    none

5. calcular_costos_restock(stocks, precios, stock_minimo=10, margen_flete= 0.05)

#Parametros: 
    stocks(dict): Inventario actual de productos.
    precios(dict): Precios unitarios de costo de cada producto.
    stock_minimo(int,opcional): Limite para activar el restock. Valor por defecto: 0.05(5%).

#Retorno:
    (tuple) (costo_subtotal_global, costo_gran_total)
        costo_subtotal_global(float): Suma del costo de todos los repuestos a encargar.
        costo_gran_total(float): Costo total incluyendo el marrgen de flete.