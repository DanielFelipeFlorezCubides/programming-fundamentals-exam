# Desarrolle el código fuente de un programa que permita ingresar cinco voltajes, 
# obtener su promedio y visualizar "ALTO VOLTAJE", si su promedio es mayor a 220, 
# caso contrario sea menor mostrar "VOLTAJE CORRECTO".

voltajeSuma = 0
voltajes = 0

for i in range(5):
    voltajes = float(input(f'Por favor ingrese el voltaje numero {i+1}: '))
    voltajeSuma = voltajes + voltajeSuma
    

promedio = voltajeSuma / 5
print(f'Suma de voltajes {voltajeSuma}')

if promedio > 220:
    print('ALTO VOLTAJE')
else:
    print('VOLTAJE CORRECTO')