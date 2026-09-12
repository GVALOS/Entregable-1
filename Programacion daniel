def calcular_costos_restock (stocks, precios, stock_minimo=10, margen_flete=0.05):

    print("/" + "="*50)
    print(" REPORTE DE COSTOS DE RESTOCK")
    print("="*50)

    costo_subtotal_global = 0.0
    se_requiere_restock = False

    for producto, cantidad_actual in stocks.items():
        precio_costo = precios.get(producto, 0.0)
        
    if cantidad_actual <= stock_minimo:
            se_requiere_restock = True
            meta_inventario = stock_minimo * 2
            cantidad_a_pedir = meta_inventario - cantidad_actual
            costo_subtotal = cantidad_a_pedir * precio_costo
            costo_subtotal_global += costo_subtotal

    print(f"Producto: {producto.upper()}")
    print(f" > Stock actual: {cantidad_actual}| Minimo: {stock_minimo}")
    print(f" > Piezas a reponer: {cantidad_a_pedir} unidades")
    print(f" > Costo unitario: ${precio_costo:.2f}")
    print(f" > Subtotal restock: ${costo_subtotal:.2f}")
    print("-"*50)


    if not se_requiere_restock:
        print("Todos los productos tienen suficiente stock. No se requiere inversion de restock.")
        return 0.0, 0.0

    costo_total_flete = costo_subtotal_global * margen_flete
    costo_gran_total = costo_subtotal_global + costo_total_flete

    print(f"SUBTOTAL NETO DE COMPRAS: ${costo_subtotal_global:.2f}")
    print(f"FLETE Y LOGISTICA ({int(margen_flete*100)}%): ${costo_total_flete:.2f}")
    print(f"COSTO TOTAL ESTIMADO RESTOCK: ${costo_gran_total:.2f}")
    print("="*50 + "/n")

    return costo_subtotal_global, costo_gran_total