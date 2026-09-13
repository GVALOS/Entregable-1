#Sistema de Gestión de Inventario y Restock de Repuestos

##Descripción del programa
Este programa en Python permite gestionar el inventario de una tienda de repuestos. Integra funciones para controlar el nivel de stock de los productos, realizar transacciones de compra/descuento de inventario, registrar nuevos repuestos y calcular de forma automática el costo necesario para finalizar el reabastecimiento considerando fletes y logística.

##Integrantes del Equipo y Aportes

|Pedro Reyes|Evaluacion de Inventario| Comprobó las existencias del stock y dio a conocer la necesidad del restock.|

|Rodrigo Gestión de Restock y Compras| Implemento las funciones para procesar transacciones de compra, registrar nuevos productos y el menú interactivo.|

|Daniel Brizuela| Analisis Financiero de Restock| Desarolle el calculo de cosotos de reabastecimiento, subtotales por repuesto y estimacion con flete.|

|Pedro Valle| Pruebas/Aseguramiento de calidad| Encargado de realizar las pruebas de codigo y vereficar casos de borde (ej. stock insuficiente, opciones invalidas).|

|Gabriel Avalos| Revisor de Codigo y Control de github| Encargado de revisar y modificar el codigo segun las instrucciones dadas, ademas de verificar la correcta integracion del codigo y publicacion del repositorio en Github.|

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
Evalua la cantidad actual de un producto e imprime una advertencia en consola segun el limite minimo definido.

#parametros:

-producto(str): Nombre o identificador del repuesto.

-stock_act(int): Cantidad actual disponible en el inventario.

-stock_min(int):Cantidad minima requerida de inventario.

#retorno:
    none

2. compra(producto, cantidad, stock_act)
Procesa la reduccion de inventario tras una ventana o consumo.

#Parametros:

-producto(str): Nombre del repuesto a comprar.

-cantidad(int): Unidades que se desean comprar.

-stock_act(int): Cantidad disponible actualmente.

#Retorno:
    (tuple) (nuevo_stock, exito)
    
-nuevo_stock(int): Cantidad restante tras la transaccion

-exito(bool): True si la compra fue exitosa, False si el stock fue insuficiente.

3. resgistrar_producto(lista_productos, stocks)
Permite al usuario agregar un nuevo repuesto al catalago mediante entradas por consola.

#Parametros:

-lista_productos(list): Lista con los nombres de los productos registrados

-stocks(dict): Diccionario que asocia el nombre del producto con su cantidad disponible.

#Retorno:
    none

4. comprar(lista_productos, stocks, compras)
Maneja la interaccion de compra con el usuario, validando la existencia del producto y actualizando el historial de transacciones.
#Parametros:

-lista_productos(list): Productos registrados en el sistema.

-stocks(dict): Registro de inventario actual.

-compras(list): Historial donde se almacenan las compras realizadas (producto, cantidad).

#Retorno:
    none

5. calcular_costos_restock(stocks, precios, stock_minimo=10, margen_flete= 0.05)
Analiza que productos estan en o por debajo del stock minimo, calculo cuantos unidades se deben reponer para duplicar el stock minimo y proyecta los costos subtotales y totales considerando un porcentaje de flete.

#Parametros: 

-stocks(dict): Inventario actual de productos.

-precios(dict): Precios unitarios de costo de cada producto.

-stock_minimo(int,opcional): Limite para activar el restock. Valor por defecto: 0.05(5%).

#Retorno:
    (tuple) (costo_subtotal_global, costo_gran_total)
    
-costo_subtotal_global(float): Suma del costo de todos los repuestos a encargar.

-costo_gran_total(float): Costo total incluyendo el marrgen de flete.
