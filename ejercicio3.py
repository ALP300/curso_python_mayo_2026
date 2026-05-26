import datetime

def verificar_bisiesto_y_edad():
    print("==============================================")
    print("       VERIFICACIÓN DE AÑO Y EDAD LEGAL       ")
    print("==============================================")

    # Obtener el año actual del sistema
    anio_actual = datetime.datetime.now().year

    # Solicitar y validar el año de nacimiento
    while True:
        try:
            anio_nacimiento = int(input("Ingrese su año de nacimiento (ej. 2005): "))
            if 1900 <= anio_nacimiento <= anio_actual:
                break
            elif anio_nacimiento > anio_actual:
                print(f"Error: El año de nacimiento no puede ser mayor que el año actual ({anio_actual}).")
            else:
                print("Error: Por favor, ingrese un año válido (a partir de 1900).")
        except ValueError:
            print("Error: Por favor, ingrese un valor numérico entero.")

    print("\n================ RESULTADOS ================")

    # 1. Determinar si el año de nacimiento es bisiesto
    # Regla: Un año es bisiesto si es divisible por 4 y no por 100, excepto si es divisible por 400.
    if (anio_nacimiento % 4 == 0 and anio_nacimiento % 100 != 0) or (anio_nacimiento % 400 == 0):
        es_bisiesto = True
        print(f"El año {anio_nacimiento}: ¡Es un año BISIESTO! 📅")
    else:
        es_bisiesto = False
        print(f"El año {anio_nacimiento}: NO es un año bisiesto. 📅")

    # 2. Calcular la edad del usuario
    edad = anio_actual - anio_nacimiento
    print(f"Edad calculada (al año {anio_actual}): {edad} años.")

    # 3. Verificar si es mayor de edad (18 años o más)
    if edad >= 18:
        print("Estado legal: MAYOR DE EDAD (18+) ✓")
    else:
        anios_restantes = 18 - edad
        print(f"Estado legal: MENOR DE EDAD ✗ (Faltan {anios_restantes} año(s) para la mayoría de edad).")

    print("==============================================")

if __name__ == "__main__":
    verificar_bisiesto_y_edad()
