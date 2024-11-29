
opcion = 0

while opcion != 6:

    print('Bienvenido las opciones son')
    print('1. Crea un libro')
    print('2. Actualizar un libro')
    print('3. Eliminar un Libro')
    print('4. Consultar un libro')
    print('5. Mostrar todo el inventario')

    opcion = int(input('Ingrese una opcion'))

    if opcion == 1:
        print('Vamo a crear: ')
    elif opcion == 2:
        print('Vamo a actualizar: ')
    elif opcion == 3:
        print('Vamo a eliminar: ')
    elif opcion == 4:
        print('Vamo a consultar: ')
    elif opcion == 5:
        print('Vamo a elimiar: ')
    elif opcion == 6:
        print('Hasta pronto')
    else:
        print('Opcion invalida: ')
