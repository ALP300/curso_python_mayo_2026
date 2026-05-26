'''
Verificación de año bisiesto y edad legal:
Pide el año de nacimiento y determina si es bisiesto. Luego calcula la edad del usuario
y verifica si es mayor de edad (18+).
'''
print("===== AÑO BISIESTO Y MAYORÍA DE EDAD =====")

anio = int(input("Ingrese su año de nacimiento: "))
anio_actual = 2026

# Verificar si es bisiesto
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

# Calcular edad
edad = anio_actual - anio

print("Su edad es:", edad)

# Verificar mayoría de edad
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")