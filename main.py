# Desarrolle un programa que solicite ingrese tres voltajes distintos e 
# indique si el promedio de los voltajes ingresados es menor a 115 visualice "VOLTAJE CORRECTO", 
# caso contrario sea mayor a 115 y menor a 220 visualice "ALTO VOLTAJE", y si es mayor a 220 visualice "PELIGRO".

voltajeSuma = 0
voltajes = 0

for i in range(3):
    voltajes = float(input(f'Por favor ingrese el voltaje numero {i+1}: '))
    voltajeSuma = voltajes + voltajeSuma
    

promedio = voltajeSuma / 3
print(f'Suma de voltajes {voltajeSuma}')

if promedio < 115:
    print('VOLTAJE CORRECTO')
elif promedio >= 115 and promedio < 220:
    print('ALTO VOLTAJE')
else:
    print("PELIGRO")