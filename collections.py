"""
Lista

Una coleccion ordenada de elementos
cualquier tipo dato puede ser
un elemento
Es mutable
Acepta elementos repetidos

Usamos corchetes y se separamos
por comas


"""

myfruitlist = ["Pera", "Banana", "Mango"]
print(myfruitlist)
print(type(myfruitlist))

# Acceder a un elemento por posicion

# Mientra el primer elemento

print(myfruitlist[0])

# Mientra el segundo elemento

print(myfruitlist[1])

# Mientra el tercero elemento

print(myfruitlist[2])

### cambio la banana por un melon

myfruitlist[2] = "melon"


# Metodos de las listas

# appednd

myfruitlist.append("uva")

print(myfruitlist)


""" Tupla 

Es una coleccion INMUTABLE ordenada
de elementos
Se usan parentesis y separamos
por comas


"""


myfruit_tuple = ("Pera", "Banana", "Mango")
print(myfruit_tuple)
print(type(myfruit_tuple))



""" Diccionarios
Coleccion ordenada de elementos
{ clave valor }
Mutables

clave : entero o string (unica)

valor : cualquier tipo dato (sobreescribe el ultimo)


"""


fondosrestart = {
    "mario" : "amarillo",
    "luna" : "naranja",
    "jorge" : "negro",
    "matias" : "blanco"
}

print(fondosrestart)

print(type(fondosrestart))

# me trae el fondo de  jorge
print(fondosrestart["jorge"])

#agregar un valor solo creando clave
fondosrestart["gustavo"] = "gris"

print(type(fondosrestart))








