# Desarrolle el código fuente de un programa que permita ingresar y leer el valor 
# correspondiente a una distancia en metros y la visualice expresadas en km.
# Para convertir metros a kilómetros, puedes usar la siguiente fórmula: Kilometros = metros / 1000

metros = float(input('Por favor ingrese la distancia en metros para convertirla a kilometros: '))
kilometros = metros / 1000

print(f'La distancia {metros} m convertida a kilometros es: {kilometros} km')