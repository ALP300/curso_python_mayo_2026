def clasificar_productos():
    print("==============================================")
    print("        CLASIFICACIÓN DE PRODUCTOS Y TASAS    ")
    print("==============================================")

    # 1. Solicitar y validar el nombre del producto
    while True:
        nombre = input("Nombre del producto: ").strip()
        if nombre:
            break
        print("Error: El nombre del producto no puede estar vacío.")

    # 2. Solicitar y validar el precio base
    while True:
        try:
            precio_base = float(input("Precio base ($): "))
            if precio_base > 0:
                break
            print("Error: El precio debe ser un valor numérico mayor a 0.")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

    # 3. Solicitar y validar la categoría
    categorias_permitidas = ["tecnología", "alimentos", "ropa"]
    while True:
        categoria = input("Categoría (tecnología, alimentos, ropa): ").strip().lower()
        # Normalización para facilitar la entrada del usuario
        if categoria == "tecnologia":
            categoria = "tecnología"
            
        if categoria in categorias_permitidas:
            break
        print("Error: Categoría inválida. Elija entre 'tecnología', 'alimentos' o 'ropa'.")

    # 4. Clasificar y calcular impuestos usando lógica condicional
    tasa_impuesto = 0
    clasificacion = ""

    if categoria == "alimentos":
        # Productos de primera necesidad vs premium
        if precio_base <= 50:
            clasificacion = "Básico (Primera Necesidad)"
            tasa_impuesto = 0  # Exento
        else:
            clasificacion = "Alimento Gourmet / Premium"
            tasa_impuesto = 5  # 5% impuesto

    elif categoria == "ropa":
        # Ropa común vs moda o lujo
        if precio_base <= 150:
            clasificacion = "Prenda de Vestir Básica"
            tasa_impuesto = 10  # 10% impuesto
        else:
            clasificacion = "Moda Exclusiva / Lujo"
            tasa_impuesto = 18  # 18% impuesto

    elif categoria == "tecnología":
        # Tecnología estándar vs alta gama
        if precio_base <= 500:
            clasificacion = "Tecnología Estándar / Consumo"
            tasa_impuesto = 15  # 15% impuesto
        else:
            clasificacion = "Tecnología de Alta Gama / Lujo"
            tasa_impuesto = 22  # 22% impuesto

    # 5. Cálculos finales
    monto_impuesto = precio_base * (tasa_impuesto / 100)
    precio_final = precio_base + monto_impuesto

    # 6. Mostrar el resumen detallado
    print("\n================ RESUMEN DE CLASIFICACIÓN ================")
    print(f"Producto:       {nombre.title()}")
    print(f"Categoría:      {categoria.capitalize()}")
    print(f"Clasificación:  {clasificacion}")
    print(f"Precio Base:    ${precio_base:.2f}")
    print(f"Impuesto ({tasa_impuesto}%): ${monto_impuesto:.2f}")
    print(f"Precio Final:   ${precio_final:.2f}")
    print("==========================================================")

if __name__ == "__main__":
    clasificar_productos()
