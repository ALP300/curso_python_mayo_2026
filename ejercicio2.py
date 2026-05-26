def validar_acceso():
    print("==============================================")
    print("          SISTEMA DE CONTROL DE ACCESO        ")
    print("==============================================")

    # Base de datos simulada de credenciales y roles registrados
    usuarios_db = {
        "admin1": {"password": "admin123", "rol": "admin"},
        "editor1": {"password": "editor123", "rol": "editor"},
        "visitante1": {"password": "visitante123", "rol": "visitante"}
    }

    # Solicitar credenciales al usuario
    usuario_input = input("Ingrese su usuario: ").strip()
    contrasena_input = input("Ingrese su contraseña: ").strip()
    rol_input = input("Ingrese su rol (admin, editor, visitante): ").strip().lower()

    print("\n================ VERIFICACIÓN ================")

    # 1. Verificar si el usuario existe en el sistema
    if usuario_input in usuarios_db:
        datos_usuario = usuarios_db[usuario_input]
        
        # 2. Verificar si la contraseña es correcta (Lógica anidada)
        if contrasena_input == datos_usuario["password"]:
            
            # 3. Verificar si el rol ingresado coincide con el rol de su cuenta (Lógica anidada)
            if rol_input == datos_usuario["rol"]:
                print(f"¡Acceso CONCEDIDO! Bienvenido(a), {usuario_input}.")
                print(f"Rol Activo: {rol_input.upper()}")
                print("\nPermisos y accesos disponibles:")
                
                # Múltiples condicionales para determinar los permisos según el rol
                if rol_input == "admin":
                    print("- [✓] Acceso total y sin restricciones a la base de datos.")
                    print("- [✓] Crear, suspender y eliminar cuentas de usuario.")
                    print("- [✓] Modificar configuraciones globales del sistema.")
                    print("- [✓] Publicar, editar y borrar cualquier tipo de contenido.")
                elif rol_input == "editor":
                    print("- [✓] Crear y editar artículos y publicaciones.")
                    print("- [✓] Gestionar y moderar comentarios de visitantes.")
                    print("- [✓] Subir archivos multimedia al servidor.")
                    print("- [✗] Sin privilegios de administración o de cuentas de usuario.")
                elif rol_input == "visitante":
                    print("- [✓] Visualizar y leer todos los contenidos publicados.")
                    print("- [✓] Escribir comentarios en las publicaciones.")
                    print("- [✓] Descargar recursos públicos de lectura.")
                    print("- [✗] Sin permisos de edición ni modificación del sistema.")
                else:
                    print("- [!] Rol reconocido pero sin permisos específicos asignados.")
            
            else:
                # El usuario y contraseña son correctos, pero el rol ingresado es erróneo
                print("Acceso DENEGADO.")
                print(f"Error de Autorización: El rol '{rol_input}' no coincide con el asignado a este usuario.")
                
        else:
            # El usuario existe pero la contraseña es incorrecta
            print("Acceso DENEGADO.")
            print("Error de Autenticación: Contraseña incorrecta.")
            
    else:
        # El usuario no existe en la base de datos
        print("Acceso DENEGADO.")
        print("Error de Autenticación: El usuario ingresado no existe en el sistema.")

    print("==============================================")

if __name__ == "__main__":
    validar_acceso()
