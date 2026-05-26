'''
Clasificación de productos:
Pide nombre, precio y categoría (tecnología, alimentos, ropa). Dependiendo de la
categoría y precio, aplica diferentes tipos de impuestos y clasificaciones (lujo, básico,
etc.).
'''
print("===== CLASIFICACIÓN DE PRODUCTOS =====")

nombre = input("Ingrese nombre del producto: ")
precio = float(input("Ingrese precio: "))
categoria = input("Ingrese categoría (tecnologia/alimentos/ropa): ")

# Categoría tecnología
if categoria == "tecnologia":

    impuesto = precio * 0.18
    total = precio + impuesto

    print("\nCategoría: Tecnología")

    if precio > 3000:
        print("Clasificación: Lujo")
    else:
        print("Clasificación: Básico")

# Categoría alimentos
elif categoria == "alimentos":

    impuesto = precio * 0.05
    total = precio + impuesto

    print("\nCategoría: Alimentos")

    if precio > 100:
        print("Clasificación: Premium")
    else:
        print("Clasificación: Básico")

# Categoría ropa
elif categoria == "ropa":

    impuesto = precio * 0.10
    total = precio + impuesto

    print("\nCategoría: Ropa")

    if precio > 500:
        print("Clasificación: Exclusiva")
    else:
        print("Clasificación: Económica")

else:
    print("Categoría no válida")

print("Impuesto:", impuesto)
print("Precio total:", total)