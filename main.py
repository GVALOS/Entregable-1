from funciones import user

lista_productos = [
    "repuesto1",
    "repuesto2",
    "repuesto3",
    "repuesto4"
]

stocks = {
    "repuesto1": 20,
    "repuesto2": 20,
    "repuesto3": 20,
    "repuesto4": 20
}

precios = {
    "repuesto1": 15.00,
    "repuesto2": 20.00,
    "repuesto3": 10.00,
    "repuesto4": 25.00
}

compras = []

while True:
    user(lista_productos, stocks, compras, precios)

    print("\n" + "=" * 50)
    print("          PROCESO FINALIZADO")
    print("=" * 50)

    while True:
        respuesta = input("¿Desea volver a ejecutar el programa? (s/n): ").strip().lower()

        if respuesta == "s":
            print("\nReiniciando el programa...\n")
            break

        elif respuesta == "n":
            print("\nGracias por utilizar el sistema.")
            print("Programa terminado.")
            exit()

        else:
            print("Respuesta inválida. Escriba 's' o 'n'.")