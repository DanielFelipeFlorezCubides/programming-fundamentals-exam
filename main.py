# Desarrolle el código fuente de un programa que permita calcular el área de un triángulo equilátero, 
# adicional visualizar "DATOS NO VÁLIDOS", si el área es mayor a 1000.
# Explicación:
# Un triángulo equilátero tiene todos sus lados iguales, y sus ángulos interiores son todos de 60 grados.
# Esta fórmula se deriva usando trigonometría y geometría básica aplicadas a un triángulo equilátero.
import math
lado = float(input('Dame la longitud de un lado del triangulo: '))

area = (((math.sqrt(3))/4)* math.pow(lado, 2))

if area > 1000:
    print('DATOS NO VÁLIDOS')
else:
    print(f'El area del triangulo es: {area}')