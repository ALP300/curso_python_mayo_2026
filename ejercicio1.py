'''
Sistema de clasificación de rendimiento: 
Solicita al usuario su nota (0-20) y su asistencia (%). Si la nota es mayor o igual a 11 y 
la asistencia es mayor o igual al 70%, se aprueba. De lo contrario, se desaprueba. 
Además, otorga menciones especiales para notas mayores a 17 con asistencia completa. 
'''
#SOY UN COMENTARIO
#Solicita la nota
nota= int(input("Ingresa tu nota: "))
#Solicita la asistencia
asistencia= int(input("Ingresa tu asistencia: "))
#Comprueba si el alumno esta aprobado
if nota>=11 and asistencia>=70:
    print("Aprobado")
    #Comprueba si el alumno tiene una men
    if nota>17 and asistencia==100:
        print("Mención de honor")
    else:
        print("Sin mención")
else:
    print("Desaprobado")
    