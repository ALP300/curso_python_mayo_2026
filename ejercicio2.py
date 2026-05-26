'''
Validación de acceso:
Solicita usuario, contraseña y rol (admin, editor, visitante). Verifica si las credenciales
son válidas y muestra los permisos disponibles según el rol. Usa múltiples condicionales
y lógica anidada.
'''
print("=== VALIDACIÓN DE ACCESO ===")
usuario = input("Ingrese usuario: ")
contrasena = input("Ingrese contraseña: ")
rol = input("Ingrese rol (admin/editor/visitante): ")

# Validación de credenciales
if usuario == "admin" and contrasena == "1234":
    print("\nCredenciales válidas")

    # Validación de roles
    if rol == "admin":
        print("Permisos:")
        print("- Acceso total")
        print("- Gestionar usuarios")
        print("- Editar contenido")

    elif rol == "editor":
        print("Permisos:")
        print("- Editar contenido")
        print("- Publicar información")

    elif rol == "visitante":
        print("Permisos:")
        print("- Solo lectura")

    else:
        print("Rol no válido")

else:
    print("\nUsuario o contraseña incorrectos")