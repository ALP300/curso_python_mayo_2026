def clasificar_rendimiento():
    print("==============================================")
    print("   SISTEMA DE CLASIFICACIÓN DE RENDIMIENTO    ")
    print("==============================================")
    
    # Solicitar y validar la nota (debe estar entre 0 y 20)
    while True:
        try:
            nota = float(input("Ingrese su nota (0-20): "))
            if 0 <= nota <= 20:
                break
            else:
                print("Error: La nota debe estar entre 0 y 20.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
            
    # Solicitar y validar la asistencia (debe estar entre 0 y 100)
    while True:
        try:
            asistencia = float(input("Ingrese su porcentaje de asistencia (0-100%): "))
            if 0 <= asistencia <= 100:
                break
            else:
                print("Error: La asistencia debe estar entre 0% y 100%.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
            
    print("\n================ RESULTADO ================")
    
    # Determinar si aprueba
    # Aprobado si: nota >= 11 y asistencia >= 70%
    if nota >= 11 and asistencia >= 70:
        print("Estado: APROBADO")
        
        # Mención especial si nota > 17 y asistencia completa (100%)
        if nota > 17 and asistencia == 100:
            print("¡Mención Especial! Excelente rendimiento académico y asistencia perfecta.")
    else:
        print("Estado: DESAPROBADO")
        
        # Opcional: indicar brevemente la razón de la desaprobación
        razones = []
        if nota < 11:
            razones.append("nota menor a 11")
        if asistencia < 70:
            razones.append("asistencia menor al 70%")
        print(f"Motivo: No cumple con los requisitos mínimos ({' y '.join(razones)}).")
        
    print("===========================================")

if __name__ == "__main__":
    clasificar_rendimiento()
    