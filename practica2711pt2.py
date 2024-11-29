""" 26/100 INTERCAMBIA VALORES DE DOS VARIABLES CON
           ASIGNACION MULTIPLE
"""
a = 5
b = 10

a, b = b, a

print( a, b)


""" 27/100 REALIZA OPERACIONES BASICAS CON CONJUNTOS
           UNION E INTERSECCION
"""
conjunto1 = {1,2, 3}
conjunto2 = {3, 4, 5}

union = conjunto1 | conjunto2 
# union | junta las variables y sobre pone
print("El conjunto es:", union)

interseccion = conjunto1 & conjunto2
# interseccion indica cual numero topa entre las variables 
print("La interseccion se encuentra en:", interseccion)



""" 28/100 EXTRAE UN ELEMENTO ESPECIFICO DE UNA TUPLA """

tupla = (10, 20, 30)
elemento = tupla[1]
#si se pide tupla[1] deberia entregar 20 por las posiciones 0, 1, 2

print("El elemento extraido es:", elemento)


""" 29/100 COMBINA DOS LISTAS EN ÁRES USANDO FUNCION ZIP"""

lista1 = [1,2,3]
lista2 = ['a','b','c']

pares = list(zip(lista1, lista2)) 
# zip junta listas por pares
print(pares)




""" 30/100 ELIMINA DUPLICADOS DE UNA LISTA """

lista1 = [1, 2, 2, 3, 4, 4, 5]
sin_duplicados = list(set(lista1))
# set elimina duplicados de las listas
print("La lista sin duplicados es:", sin_duplicados)


""" 31/100 PIDE UN NRO Y VERIF SI ES POSITIVO NEG o 0  """

numero = int(input("Escribe un nro: "))

if numero > 0:
    print('Positivo')
elif numero < 0:
    print('Negativo')
else:
    print('Es cero')
    
    
""" 32/100 PIDE UN NRO Y COMPRUEBA SI EL NUMERO ES 
           PAR o IMPAR USANDO IF MODULO 
"""

numero = int(input('Ingrese un nro: '))

if numero % 2 == 0:
    print("El numero es par")
elif numero % 2 != 0:
    print("El nro es impar")
    
    
"""     33/100 DETERMINE SI UN AÑO ES BISIESTO
REGLA
    - DIVISIBLE POR 4
    - NO DIVISIBLE POR 100
    - DIVISIBLE POR 400

"""


anio = 2024

if (anio % 4 == 0 and anio % 100 != 0) or \
    (anio % 400 == 0):
    print("Es un año bisiesto")
else:
    print("No es bisiesto")
    
    
""" 34/100   VERIFICA SI UNA CADENA ES 
           MAYOR O IGUAL A 10 CARACTERES
"""
    
cadena = 'Hola que tal'

if len(cadena) >= 10:
    print("Cadena tiene 10 o mas caracteres")
else:
    print("La cadena tiene menos de 10 caracteres")
    
    
""" 35/100 COMPUEBA SI UN NRO ESTA EN EL RANGO DE 1 A 100"""

numero = 88

if 1 <= numero <= 100:
    print('Esta en el rango de 1 a 100')
else:
    print('No esta en el rango de 1 a 100')
    
    
"""  36/100 PIDE CARACTER Y DETERMINE SI ES VOCAL """

caracter = input('Ingrese caracter: ')
vocales = ['a','e','i','o','u']

if caracter.lower in vocales:
    print("La letra es una vocal")
else:
    print("La letra no es una vocal")
    
    
""" 37/100 CALCULA EL MAXIMO DE 3 NUMEROS """


num1 = 5
num2 = 60
num3 = 23

maximo = max(num1, num2, num3)
#funcion max sirve para saber el mayor

print("El mayor nro es: ", maximo)


""" 38/100  DETERMINA SI UN NRO ES DIVISI ENTRE 5 Y 7"""

num = 35

if num % 5 == 0 and num % 7 == 0:
    print('Numero SI es divisible entre 5 y 7')
else:
    print('Numero NO es divisible entre 5 y 7')


""" 39/100 VERIFICA SI LA PALABRA INGRESADA ES PYTHON"""

palabra = str(input('Ingrese una palabra:'))


if palabra.lower() == 'python':
    print('La palabra SI es Phyton')
else:
    print('La palabra NO es Python')
    

""" 40/100 CALCULAR EL IMC E INTERPRETARLO"""

peso = 70
altura = 1.75
imc= peso / (altura ** 2)
print("El IMC es : ", imc)

if imc < 18.5:
    print('bajo peso')
elif imc < 25:
    print('peso normal')
elif imc < 30:
    print('sobrepeso')
elif imc < 35:
    print('obesidad grado I')
elif imc < 40:
    print('obesidad grado II')
else:
    print('Obesidad grado III')
    
    
""" 41/100 IMPRIME NROS DEL 10 AL 1 EN ORDEN DESCENDENTE  """

contador = 10

while contador > 0:
    print(contador)
    contador -= 1
    
    
""" 42/100 SOLICITA INGRES NRO N Y LUEGO 
           IMPREME SUMA DE 1 HASTA N
"""
    
numero = int(input('Ingresa numero'))    
suma = 0
i = 1

while i <= numero:
    suma += i 
    i += 1
print('La suma es: ', suma)


""" 43/100 SOLICIA ING UN NUMERO N E IMPRIME FACTORIAL DE ESE NUM"""

numero = int(input('Ingrese un Numero: '))
factorial = 1
i =1

while i <= numero:
    factorial = factorial * i 
    i = i + 1
print('el factorial es: ', factorial)



"""44/100 GENERA NRO ALEATORIO DE 1-10 LUEGO PIDE A USUARIO 
          ADIVINAR EL NRO HASTA QUE LO HAGA CORRECTAMENTE
"""

import random
numero_secreto = random.randint(1, 10)
intentos = 0

while True:
    intento = int(input('Adivine un nro del 1 al 10: '))
    intentos = intentos + 1
    if intento == numero_secreto:
        print(f'Adivinaste, tomo {intentos} intentos')
        break









