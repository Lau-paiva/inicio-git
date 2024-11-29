""" EJERCICIO BASICO: HOLA MUNDO """

print("Hola mundo")


""" SUMAR DOS NUMEROS """

variable1 = 5
variable2 =6
suma = variable1 + variable2


print("Total es :", suma) 
print("La suma de", variable1, "+", variable2, "=", suma)

""" MOSTRAR PRECIO IVA CON VALOR 100 """

iva = 0.19
precio_producto = 2500
precio_iva = iva * precio_producto

print("El iva es: ", precio_iva)
print("El precio final es:", (precio_iva + precio_producto) )


""" DE DOS NROS SABER CUAL ES EL MAYOR """

nro1 = 5
nro2 = 7

if (nro1 <= nro2 ):
    print( nro1, "es menor que ", nro2)
else:
    print( nro2, "es mayor que ", nro1)

""" USANDO AND """

numero = 11

if (numero>=1 and numero<=10):
    print("Esta entre 1 y 10")
else: 
    print("no esta en ese rango")


""" SUMAR DOS NROS  """
nro1 = 1
nro2 = 2
resultado = nro1 + nro2

print("El resultado es:", resultado)

""" CALCULA EL AREA DE UN CIRCULO CON UN RADIO DADO """

import math

radio = 3
area = math.pi * radio**2
print("El area es: ", area)


""" CONCATENA 2 CADENA DE TEXTO"""

cadena1 = "Hola"
cadena2 = "Mundo"

concatenacion = cadena1 + " " + cadena2 

print("La cadena de texto final es: ", concatenacion)


""" CREA UNA LISTA CON DIF ELEMENTOS E IMPRIMELA """

listasuper = [1, 'cebolla', 2.34,  'tomate', True,  'ajo', 'pimenton']

print(listasuper)

""" REALIZA MULTIPLICACION DE DOS NROS Y MUESTRA RESULTADO"""

nro1 = 2
nro2 = 3
resultado = nro1 * nro2

print("Resultado es:", resultado)


""" CREA CADENA Y MUESTRA LONGITUD """
cadena = "Hola"
longitud = len(cadena) # len para calcular lingutud de cadena texto

print("Longitud cadena es:", longitud)


""" PROMEDIO DE UNA LISTA DE NUMEROS"""

numeros = [1, 2, 3, 4, 5, 6, 7]
promedio = sum(numeros) / len(numeros)

print("El promedio es: ", promedio)


""" 8/100 CREA TUPLA CON ELEMENTO E IMPRIMELA """

tupla = (3, False, 'uno, 3.45')

print("La tupla es: ", tupla)


""" 9/100 REALIZA POTENCIA DE UN NRO """

base = 5
exponente = 2
resultado = base ** exponente

print(f"La potencia del nro es: {base} elevado ** a {exponente} =", resultado )


""" 10/ 100 INVERTIR UNA CADENA"""

cadena = "Laura"
invertir = cadena [::-1]

print("La cadena inversa es: ", invertir)


""" 11/100  CALCULA BASE RECTANGULO Y PIDE
            BASE Y ALTURA AL USUARIO
"""

base = int(input("Ingrese base: "))
altura = int(input("Ingrese altura: "))
area_rectangulo = base * altura

print(f"Area de rectangulo es {base} * {altura} = {area_rectangulo}")



""" 12/100 CONVIENRE NRO ENTERO A CADENA """

numero = 40
print(type(numero))
cadena =str(numero)
print(type(cadena))



""" 13/100 REEMPLAZA 1 CARACTER EN UNA CADENA """


cadena = "Python"
nueva_cadena = cadena.replace("o", "x")

print("nueva cadena: ", nueva_cadena)


""" 14/100 PASA UNA CADENA DE MAYUS A MINUSC  """

mayus = 'PYTHON'
minus = mayus.lower() #lower para pasar de mayuscula a minuscula

print("minusculas", minus)


""" 14.2/100 """

minus = 'python'
mayus = minus.upper() # upper para pasar de minuscula a mayuscula

print("Mayusculas", mayus)


""" 15/100 ORDENA LISTA DE MAYOR A MENOR """

lista = [7, 2, 5, 1, 9]
lista.sort() # ordena automac de mayor a menor

print("Lista final es :", lista)



""" 16/100 CALCULA 2 ELEVADO A 4 SIN USAR **  """

resultado = pow(2,4)
print("Resultado elevado es: ", resultado)



""" 17/100 EXTRAE UNA CADENA DE UNA SUB CADENA DADA """

cadena = str(input("Ingrese una palabra: "))
subcadena = cadena[0:3] 
# usan palabra CADENA deberia mostrar CAD 
# se una corchete y : para indicar de donde a donde mostrar
print("La subcadena es: ", subcadena)


""" 18/100 CONVIERTE NRO DECIMAL A ENTERO"""

decimal = 8.55
entero = int(decimal)

print("La conversion a entero es: ", entero)


""" 19/100 CUENTA OCURRENCIAS DE UN CARACTER ESPECIFICO
           EN UNA CADENA
"""

cadena = 'programacion'
ocurrencias = cadena.count('a') # .count para contar lo que se le indica

print("Las ocurrencias totales serian :", ocurrencias)

cadena2 = (3, 2, 5, 3, 1, 3, 3)
ocurrencias2 = cadena2.count(3) # cuando es nro es sin comillas
print("Las ocurrencias serias: ", ocurrencias2)


""" 20/100 ENCUENTRA Y MUESTRA ULTIMO CARACTER DE UNA CADENA"""

cadena = 'python'
ultimo_caracter = cadena[-1]

print("El ultimo caracter es: ", ultimo_caracter)

""" 21/100 MULTIPLICA UNA CADENA POR NRO ENTERO """

cadena = 'hola'
multiplicado = cadena * 4

print("La multiplicacion es :", multiplicado)


""" 22/100 DIVIDE UNA CADENA EN UNA LISTA DE SUBCADENAS """

cadena = 'hola como estas'
division = cadena.split()
# separa las palabras en cada espacio
# convirtiendolas es sub cadenas
print("La subcadena es: ", division)


""" 23/100 VERIFICA SI UNA PALABRA ES UN PALINDROMO """

palabra = 'radar'

es_pa = palabra == palabra [::-1]
print("Es palindromo", es_pa)


""" 24/100 ELIMINA ELEMENTE ESPECIF DE UNA LISTA   """

lista = [1, 2, 3, 4, 5]
lista.remove(3)

print("resultado :", lista)


""" 25/100 GENERA LISTA NROS DE 1 A 200  """

numeros = list(range(1,201))

print(numeros)










