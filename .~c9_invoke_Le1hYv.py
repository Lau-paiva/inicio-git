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

caracter = input('Ingrese caracter')
vocales = [a,e,i,o,u]

if caracter.lower in vocales:
    print('Es ')
    
    









