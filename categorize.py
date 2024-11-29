"""
Ciclo FOR

- Se exactamente cuando voy a parar el cliclo
- Ideal para recorrer listas, tuplas.
diccionarios, etc. (secuencias)


"""

lista = ["dinosaurio", 23, True, 45.5, "amazon"]

# for [variable_de_iteracion]
# la x despues de FOR hace referencia
# a lo que hay dentro de la lista
# (mencionar nombre de lista)


for x in lista:
    print(f"Elemento {x} y su tipo de dato es {type(x)}")
    
    
# Dada la siguiente lista imprime SOLO los numeros pares

numeros = [2, 45, 19, 13, 178]

"""
 FORMA BASICA
 
 for x in numeros:
    if num % 2 == 0:  # Verificamos si el número es par
        print(x)  # Imprimimos el número par
 """
 

for x in numeros: print(x) if x % 2 == 0 else None
    
    
    
    
    
