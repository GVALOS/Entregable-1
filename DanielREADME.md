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
1. calcular_costos_restock(stocks, precios, stock_minimo=10, margen_flete= 0.05)

#Desarollado por: Daniel Brizuela

#Descripcion: Analiza que productos del inventario están en o por debajo del stock minimo recomendado, determina la cantidad exacta de unidades necesarias para abastecer el almacen y calcula la proyeccion financiera del restock.

#Parametros: 

-stocks(dict): Inventario con la cantidad actual disponible de cada producto.
    
-precios(dict): Precios unitarios de costo de cada producto.
    
-stock_minimo(int,opcional): Cantidad limite que determina cuando un producto requiere restock. Valor por defecto: "10".

-margen_flete(float,opcional): Porcentaje adicional por costos de envio y manejo logistico. Por defecto es "0.05" (5%).

#Retorno:
(tuple) (costo_subtotal_global, costo_gran_total)
       
-costo_subtotal_global(float): Suma del costo de todos los repuestos a encargar.

-costo_gran_total(float): Costo total incluyendo el marrgen de flete y logistica.
