"""
Ciclo WHILE
es una sentencia que repetira
un conjunto de instrucciones MIENTRAS QUE
una condicion sea verdaderas
"""

suma = 0

# Usamos un ciclo for para iterar desde el 1 hasta el 10 (inclusive)
for i in range(1, 11):
    suma += i  # Esto es lo mismo que: suma = suma + i
# Imprimimos el resultado
print("La suma de los números del 1 al 10 es:", suma)


"""



# Imprimir la tabla de multiplicar del 5
for i in range(1, 11):  # Recorremos los números del 1 al 10
    print(f"5 x {i} = {5 * i}")  # Imprimimos el resultado de la multiplicación
    
    
    
    
    
    # Pedimos al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")

# Inicializamos un contador de vocales
contador_vocales = 0

# Lista de vocales
vocales = "aeiouAEIOU"

# Recorremos cada letra de la palabra
for letra in palabra:
    # Verificamos si la letra es una vocal
    if letra in vocales:
        contador_vocales += 1  # Aumentamos el contador si es una vocal

# Imprimimos el resultado
print("La cantidad de vocales en la palabra es:", contador_vocales)


"""


suma = 0

for i in range(1,11):
    suma += i
    print("La suma es: ", suma)








    
    
    