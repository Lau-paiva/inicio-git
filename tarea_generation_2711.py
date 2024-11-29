# EJERCICIO 1
#SUMA NROS DE 1 AL 10 con ciclo for

suma = 0

for i in range(1,11):
    suma += i 
print(f'La suma es: {suma}')


# EJERCICIO 2
# TABLA MULTIPLICAR DEL 5

for i in range(1, 11): 
    resultado = 5 * i    # Multiplicamos 5 por el valor de i
print(f"5 x {i} = {resultado}")  # Imprimimos el resultado
    


# EJERCICIO 3    
#PIDE AL USUARIO UNA PALABRA Y CUENTA LAS VOCALES


#   FORMA 1
palabra = str(input('Ingrese una palabra y calcular sus vocales: '))

contador_vocales = 0

for letra in palabra:
    if letra.lower() in 'aeiou':
        contador_vocales += 1
print(f'Tiene {contador_vocales} vocales')




    
#   FORMA 2

palabra = input("Ingrese una palabra y calcular sus vocales: ")

# Inicializamos un contador de vocales
contador_vocales = 0

# Lista de vocales
vocales = "aeiouAEIOU"



for letra in palabra:
    # Verificamos si la letra es una vocal
    if letra in vocales:
        contador_vocales += 1  # Aumentamos el contador si es una vocal

# Imprimimos el resultado
print(f"Tiene {contador_vocales} vocales")



# EJERCICIO 4 
#PARA UNA LISTA DE NROS ENCONTRAR MAYOT USANDO CICLO Y CONDICIONAL
    
    
lista = [20, 12, 7, 10, 19]
mayor = lista[0]
 
for i in lista:
    if i > mayor:
         mayor = i
print(f'el nro es: {mayor} ')


"""  IMPRIME NROS HASTA Q USUARIO DIGA STOP """
     

numero = 1  # Iniciamos el contador en 1

while True:  # El ciclo se repite indefinidamente
    print(numero)  # Imprime el número actual
    numero += 1  # Aumenta el número para la siguiente iteración
# Pedimos al usuario que ingrese algo
    usuario_entrada = input("Escribe 'stop' para detener o presiona Enter para continuar: ")
    
    if usuario_entrada.lower() == 'stop':  # Verificamos si la entrada es 'stop'
        break  # Salimos del ciclo si el usuario escribe 'stop'


# EJERCICIO 6 usuario adivine un número entre 1 y 10 """

import random
numero_secreto = random.randint(1, 10)
nro_a_intento = 0

while True:
    intento = int(input('Adivine un nro del 1 al 10: '))
    nro_a_intento = nro_a_intento + 1
    if nro_a_intento == numero_secreto:
        print(f'Adivinaste, tomo {nro_a_intento} intentos')
        break
    

# EJERCICIO 7

numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print('El nro es par')
else:
    print('numero es impar')
    
    
# PIDE UN NRO

N = int(input("Introduce un número: "))

# Usamos un ciclo for para imprimir los números desde 1 hasta N
for i in range(1, N + 1):
    print(i)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    