{"changed":true,"filter":false,"title":"while.loop.py","tooltip":"/while.loop.py","value":"\"\"\"\nCiclo WHILE\nes una sentencia que repetira\nun conjunto de instrucciones MIENTRAS QUE\nuna condicion sea verdaderas\n\"\"\"\n\nsuma = 0\n\n# Usamos un ciclo for para iterar desde el 1 hasta el 10 (inclusive)\nfor i in range(1, 11):\n    suma += i  # Esto es lo mismo que: suma = suma + i\n# Imprimimos el resultado\nprint(\"La suma de los números del 1 al 10 es:\", suma)\n\n\n\"\"\"\n\n\n\n# Imprimir la tabla de multiplicar del 5\nfor i in range(1, 11):  # Recorremos los números del 1 al 10\n    print(f\"5 x {i} = {5 * i}\")  # Imprimimos el resultado de la multiplicación\n    \n    \n    \n    \n    \n    # Pedimos al usuario que ingrese una palabra\npalabra = input(\"Ingresa una palabra: \")\n\n# Inicializamos un contador de vocales\ncontador_vocales = 0\n\n# Lista de vocales\nvocales = \"aeiouAEIOU\"\n\n# Recorremos cada letra de la palabra\nfor letra in palabra:\n    # Verificamos si la letra es una vocal\n    if letra in vocales:\n        contador_vocales += 1  # Aumentamos el contador si es una vocal\n\n# Imprimimos el resultado\nprint(\"La cantidad de vocales en la palabra es:\", contador_vocales)\n\n\n\"\"\"\n\n\nsuma = 0\n\nfor i in range(1,11):\n    suma += i\n    print(\"La suma es: \", suma)\n\n\n\n\n\n\n\n\n    \n    \n    ","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":9,"column":3},"end":{"row":9,"column":4},"action":"remove","lines":[" "],"id":187},{"start":{"row":9,"column":2},"end":{"row":9,"column":3},"action":"remove","lines":["r"]},{"start":{"row":9,"column":1},"end":{"row":9,"column":2},"action":"remove","lines":["o"]},{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"remove","lines":["f"]}],[{"start":{"row":9,"column":0},"end":{"row":17,"column":53},"action":"insert","lines":["# Inicializamos una variable para guardar la suma","suma = 0","","# Usamos un ciclo for para iterar desde el 1 hasta el 10 (inclusive)","for i in range(1, 11):","    suma += i  # Esto es lo mismo que: suma = suma + i","","# Imprimimos el resultado","print(\"La suma de los números del 1 al 10 es:\", suma)"],"id":188}],[{"start":{"row":9,"column":0},"end":{"row":10,"column":8},"action":"remove","lines":["# Inicializamos una variable para guardar la suma","suma = 0"],"id":189},{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"remove","lines":["",""]},{"start":{"row":7,"column":8},"end":{"row":8,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"remove","lines":["1"],"id":190}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["0"],"id":191}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"remove","lines":["0"],"id":192}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["-"],"id":193},{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["4"]}],[{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"remove","lines":["4"],"id":194},{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"remove","lines":["-"]}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["1"],"id":195}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"remove","lines":["1"],"id":196}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["2"],"id":197}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"remove","lines":["2"],"id":198}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["1"],"id":199}],[{"start":{"row":14,"column":53},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":200},{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["",""]},{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":17,"column":0},"end":{"row":19,"column":79},"action":"insert","lines":["# Imprimir la tabla de multiplicar del 5","for i in range(1, 11):  # Recorremos los números del 1 al 10","    print(f\"5 x {i} = {5 * i}\")  # Imprimimos el resultado de la multiplicación"],"id":201}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["("],"id":202}],[{"start":{"row":19,"column":31},"end":{"row":19,"column":32},"action":"insert","lines":[")"],"id":203}],[{"start":{"row":19,"column":32},"end":{"row":19,"column":33},"action":"remove","lines":[")"],"id":204}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"remove","lines":["("],"id":205}],[{"start":{"row":11,"column":54},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":206},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]},{"start":{"row":12,"column":4},"end":{"row":13,"column":0},"action":"insert","lines":["",""]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]},{"start":{"row":13,"column":4},"end":{"row":14,"column":0},"action":"insert","lines":["",""]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"insert","lines":["",""]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":23,"column":79},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":207},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]},{"start":{"row":24,"column":4},"end":{"row":25,"column":0},"action":"insert","lines":["",""]},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]},{"start":{"row":25,"column":4},"end":{"row":26,"column":0},"action":"insert","lines":["",""]},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]},{"start":{"row":26,"column":4},"end":{"row":27,"column":0},"action":"insert","lines":["",""]},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]},{"start":{"row":27,"column":4},"end":{"row":28,"column":0},"action":"insert","lines":["",""]},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]},{"start":{"row":28,"column":4},"end":{"row":29,"column":0},"action":"insert","lines":["",""]},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]},{"start":{"row":29,"column":4},"end":{"row":30,"column":0},"action":"insert","lines":["",""]},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":27,"column":4},"end":{"row":43,"column":67},"action":"insert","lines":["# Pedimos al usuario que ingrese una palabra","palabra = input(\"Ingresa una palabra: \")","","# Inicializamos un contador de vocales","contador_vocales = 0","","# Lista de vocales","vocales = \"aeiouAEIOU\"","","# Recorremos cada letra de la palabra","for letra in palabra:","    # Verificamos si la letra es una vocal","    if letra in vocales:","        contador_vocales += 1  # Aumentamos el contador si es una vocal","","# Imprimimos el resultado","print(\"La cantidad de vocales en la palabra es:\", contador_vocales)"],"id":208}],[{"start":{"row":25,"column":4},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":209},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]},{"start":{"row":26,"column":4},"end":{"row":27,"column":0},"action":"insert","lines":["",""]},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"remove","lines":["a"],"id":210},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"remove","lines":["r"]},{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"remove","lines":["t"]},{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"remove","lines":["e"]},{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"remove","lines":["l"]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"insert","lines":["i"],"id":211}],[{"start":{"row":41,"column":11},"end":{"row":41,"column":12},"action":"remove","lines":["a"],"id":212},{"start":{"row":41,"column":10},"end":{"row":41,"column":11},"action":"remove","lines":["r"]},{"start":{"row":41,"column":9},"end":{"row":41,"column":10},"action":"remove","lines":["t"]},{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"remove","lines":["e"]},{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"remove","lines":["l"]}],[{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"insert","lines":["i"],"id":213}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"remove","lines":["i"],"id":214}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"insert","lines":["l"],"id":215},{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"insert","lines":["e"]},{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"insert","lines":["t"]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"insert","lines":["r"]},{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"insert","lines":["a"]}],[{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"remove","lines":["i"],"id":216}],[{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"insert","lines":["l"],"id":217},{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"insert","lines":["e"]},{"start":{"row":41,"column":9},"end":{"row":41,"column":10},"action":"insert","lines":["t"]},{"start":{"row":41,"column":10},"end":{"row":41,"column":11},"action":"insert","lines":["r"]},{"start":{"row":41,"column":11},"end":{"row":41,"column":12},"action":"insert","lines":["a"]}],[{"start":{"row":33,"column":1},"end":{"row":33,"column":9},"action":"remove","lines":["ontador_"],"id":218},{"start":{"row":33,"column":0},"end":{"row":33,"column":1},"action":"remove","lines":["c"]}],[{"start":{"row":42,"column":16},"end":{"row":42,"column":17},"action":"remove","lines":["_"],"id":219},{"start":{"row":42,"column":15},"end":{"row":42,"column":16},"action":"remove","lines":["r"]},{"start":{"row":42,"column":14},"end":{"row":42,"column":15},"action":"remove","lines":["o"]},{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"remove","lines":["d"]},{"start":{"row":42,"column":12},"end":{"row":42,"column":13},"action":"remove","lines":["a"]},{"start":{"row":42,"column":11},"end":{"row":42,"column":12},"action":"remove","lines":["t"]},{"start":{"row":42,"column":10},"end":{"row":42,"column":11},"action":"remove","lines":["n"]},{"start":{"row":42,"column":9},"end":{"row":42,"column":10},"action":"remove","lines":["o"]},{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"remove","lines":["c"]}],[{"start":{"row":36,"column":0},"end":{"row":36,"column":1},"action":"insert","lines":["c"],"id":220},{"start":{"row":36,"column":1},"end":{"row":36,"column":2},"action":"insert","lines":["o"]},{"start":{"row":36,"column":2},"end":{"row":36,"column":3},"action":"insert","lines":["n"]},{"start":{"row":36,"column":3},"end":{"row":36,"column":4},"action":"insert","lines":["t"]},{"start":{"row":36,"column":4},"end":{"row":36,"column":5},"action":"insert","lines":["a"]},{"start":{"row":36,"column":5},"end":{"row":36,"column":6},"action":"insert","lines":["o"]},{"start":{"row":36,"column":6},"end":{"row":36,"column":7},"action":"insert","lines":["d"]},{"start":{"row":36,"column":7},"end":{"row":36,"column":8},"action":"insert","lines":["r"]}],[{"start":{"row":36,"column":7},"end":{"row":36,"column":8},"action":"remove","lines":["r"],"id":221},{"start":{"row":36,"column":6},"end":{"row":36,"column":7},"action":"remove","lines":["d"]},{"start":{"row":36,"column":5},"end":{"row":36,"column":6},"action":"remove","lines":["o"]}],[{"start":{"row":36,"column":5},"end":{"row":36,"column":6},"action":"insert","lines":["d"],"id":222},{"start":{"row":36,"column":6},"end":{"row":36,"column":7},"action":"insert","lines":["o"]},{"start":{"row":36,"column":7},"end":{"row":36,"column":8},"action":"insert","lines":["r"]},{"start":{"row":36,"column":8},"end":{"row":36,"column":9},"action":"insert","lines":["_"]}],[{"start":{"row":36,"column":9},"end":{"row":36,"column":10},"action":"insert","lines":[" "],"id":223}],[{"start":{"row":36,"column":9},"end":{"row":36,"column":10},"action":"remove","lines":[" "],"id":224}],[{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"insert","lines":["c"],"id":225},{"start":{"row":42,"column":9},"end":{"row":42,"column":10},"action":"insert","lines":["o"]},{"start":{"row":42,"column":10},"end":{"row":42,"column":11},"action":"insert","lines":["n"]},{"start":{"row":42,"column":11},"end":{"row":42,"column":12},"action":"insert","lines":["t"]},{"start":{"row":42,"column":12},"end":{"row":42,"column":13},"action":"insert","lines":["a"]},{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"insert","lines":["o"]}],[{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"remove","lines":["o"],"id":226}],[{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"insert","lines":["d"],"id":227},{"start":{"row":42,"column":14},"end":{"row":42,"column":15},"action":"insert","lines":["o"]},{"start":{"row":42,"column":15},"end":{"row":42,"column":16},"action":"insert","lines":["r"]},{"start":{"row":42,"column":16},"end":{"row":42,"column":17},"action":"insert","lines":["_"]}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":1},"action":"insert","lines":["c"],"id":228},{"start":{"row":33,"column":1},"end":{"row":33,"column":2},"action":"insert","lines":["o"]},{"start":{"row":33,"column":2},"end":{"row":33,"column":3},"action":"insert","lines":["n"]},{"start":{"row":33,"column":3},"end":{"row":33,"column":4},"action":"insert","lines":["t"]},{"start":{"row":33,"column":4},"end":{"row":33,"column":5},"action":"insert","lines":["a"]},{"start":{"row":33,"column":5},"end":{"row":33,"column":6},"action":"insert","lines":["d"]},{"start":{"row":33,"column":6},"end":{"row":33,"column":7},"action":"insert","lines":["o"]},{"start":{"row":33,"column":7},"end":{"row":33,"column":8},"action":"insert","lines":["r"]}],[{"start":{"row":33,"column":8},"end":{"row":33,"column":9},"action":"insert","lines":["_"],"id":229}],[{"start":{"row":33,"column":9},"end":{"row":33,"column":10},"action":"insert","lines":[" "],"id":230}],[{"start":{"row":33,"column":9},"end":{"row":33,"column":10},"action":"remove","lines":[" "],"id":231}],[{"start":{"row":33,"column":8},"end":{"row":33,"column":9},"action":"remove","lines":["_"],"id":232},{"start":{"row":33,"column":7},"end":{"row":33,"column":8},"action":"remove","lines":["r"]},{"start":{"row":33,"column":6},"end":{"row":33,"column":7},"action":"remove","lines":["o"]},{"start":{"row":33,"column":5},"end":{"row":33,"column":6},"action":"remove","lines":["d"]},{"start":{"row":33,"column":4},"end":{"row":33,"column":5},"action":"remove","lines":["a"]},{"start":{"row":33,"column":3},"end":{"row":33,"column":4},"action":"remove","lines":["t"]},{"start":{"row":33,"column":2},"end":{"row":33,"column":3},"action":"remove","lines":["n"]},{"start":{"row":33,"column":1},"end":{"row":33,"column":2},"action":"remove","lines":["o"]},{"start":{"row":33,"column":0},"end":{"row":33,"column":1},"action":"remove","lines":["c"]}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":1},"action":"insert","lines":["c"],"id":233},{"start":{"row":33,"column":1},"end":{"row":33,"column":2},"action":"insert","lines":["o"]},{"start":{"row":33,"column":2},"end":{"row":33,"column":3},"action":"insert","lines":["n"]},{"start":{"row":33,"column":3},"end":{"row":33,"column":4},"action":"insert","lines":["t"]},{"start":{"row":33,"column":4},"end":{"row":33,"column":5},"action":"insert","lines":["a"]},{"start":{"row":33,"column":5},"end":{"row":33,"column":6},"action":"insert","lines":["d"]},{"start":{"row":33,"column":6},"end":{"row":33,"column":7},"action":"insert","lines":["o"]},{"start":{"row":33,"column":7},"end":{"row":33,"column":8},"action":"insert","lines":["r"]},{"start":{"row":33,"column":8},"end":{"row":33,"column":9},"action":"insert","lines":["_"]}],[{"start":{"row":36,"column":0},"end":{"row":36,"column":10},"action":"remove","lines":["contador_v"],"id":234},{"start":{"row":36,"column":0},"end":{"row":36,"column":1},"action":"insert","lines":["v"]}],[{"start":{"row":45,"column":67},"end":{"row":46,"column":0},"action":"insert","lines":["",""],"id":235},{"start":{"row":46,"column":0},"end":{"row":47,"column":0},"action":"insert","lines":["",""]},{"start":{"row":47,"column":0},"end":{"row":48,"column":0},"action":"insert","lines":["",""]},{"start":{"row":48,"column":0},"end":{"row":49,"column":0},"action":"insert","lines":["",""]},{"start":{"row":49,"column":0},"end":{"row":50,"column":0},"action":"insert","lines":["",""]},{"start":{"row":50,"column":0},"end":{"row":51,"column":0},"action":"insert","lines":["",""]},{"start":{"row":51,"column":0},"end":{"row":52,"column":0},"action":"insert","lines":["",""]},{"start":{"row":52,"column":0},"end":{"row":53,"column":0},"action":"insert","lines":["",""]},{"start":{"row":53,"column":0},"end":{"row":54,"column":0},"action":"insert","lines":["",""]},{"start":{"row":54,"column":0},"end":{"row":55,"column":0},"action":"insert","lines":["",""]},{"start":{"row":55,"column":0},"end":{"row":56,"column":0},"action":"insert","lines":["",""]},{"start":{"row":56,"column":0},"end":{"row":57,"column":0},"action":"insert","lines":["",""]},{"start":{"row":57,"column":0},"end":{"row":58,"column":0},"action":"insert","lines":["",""]},{"start":{"row":58,"column":0},"end":{"row":59,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":51,"column":0},"end":{"row":51,"column":1},"action":"insert","lines":["c"],"id":236},{"start":{"row":51,"column":1},"end":{"row":51,"column":2},"action":"insert","lines":["u"]},{"start":{"row":51,"column":2},"end":{"row":51,"column":3},"action":"insert","lines":["m"]},{"start":{"row":51,"column":3},"end":{"row":51,"column":4},"action":"insert","lines":["a"]}],[{"start":{"row":51,"column":3},"end":{"row":51,"column":4},"action":"remove","lines":["a"],"id":237},{"start":{"row":51,"column":2},"end":{"row":51,"column":3},"action":"remove","lines":["m"]},{"start":{"row":51,"column":1},"end":{"row":51,"column":2},"action":"remove","lines":["u"]},{"start":{"row":51,"column":0},"end":{"row":51,"column":1},"action":"remove","lines":["c"]}],[{"start":{"row":51,"column":0},"end":{"row":51,"column":1},"action":"insert","lines":["s"],"id":238},{"start":{"row":51,"column":1},"end":{"row":51,"column":2},"action":"insert","lines":["i"]},{"start":{"row":51,"column":2},"end":{"row":51,"column":3},"action":"insert","lines":["m"]}],[{"start":{"row":51,"column":2},"end":{"row":51,"column":3},"action":"remove","lines":["m"],"id":239},{"start":{"row":51,"column":1},"end":{"row":51,"column":2},"action":"remove","lines":["i"]}],[{"start":{"row":51,"column":1},"end":{"row":51,"column":2},"action":"insert","lines":["u"],"id":240},{"start":{"row":51,"column":2},"end":{"row":51,"column":3},"action":"insert","lines":["m"]},{"start":{"row":51,"column":3},"end":{"row":51,"column":4},"action":"insert","lines":["a"]}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":5},"action":"insert","lines":[" "],"id":241},{"start":{"row":51,"column":5},"end":{"row":51,"column":6},"action":"insert","lines":["="]}],[{"start":{"row":51,"column":6},"end":{"row":51,"column":7},"action":"insert","lines":[" "],"id":242},{"start":{"row":51,"column":7},"end":{"row":51,"column":8},"action":"insert","lines":["0"]}],[{"start":{"row":51,"column":8},"end":{"row":52,"column":0},"action":"insert","lines":["",""],"id":243},{"start":{"row":52,"column":0},"end":{"row":53,"column":0},"action":"insert","lines":["",""]},{"start":{"row":53,"column":0},"end":{"row":53,"column":1},"action":"insert","lines":["f"]},{"start":{"row":53,"column":1},"end":{"row":53,"column":2},"action":"insert","lines":["o"]},{"start":{"row":53,"column":2},"end":{"row":53,"column":3},"action":"insert","lines":["r"]}],[{"start":{"row":53,"column":3},"end":{"row":53,"column":4},"action":"insert","lines":[" "],"id":244},{"start":{"row":53,"column":4},"end":{"row":53,"column":5},"action":"insert","lines":["i"]}],[{"start":{"row":53,"column":5},"end":{"row":53,"column":6},"action":"insert","lines":[" "],"id":245},{"start":{"row":53,"column":6},"end":{"row":53,"column":7},"action":"insert","lines":["i"]},{"start":{"row":53,"column":7},"end":{"row":53,"column":8},"action":"insert","lines":["n"]}],[{"start":{"row":53,"column":8},"end":{"row":53,"column":9},"action":"insert","lines":[" "],"id":246},{"start":{"row":53,"column":9},"end":{"row":53,"column":10},"action":"insert","lines":["r"]},{"start":{"row":53,"column":10},"end":{"row":53,"column":11},"action":"insert","lines":["a"]},{"start":{"row":53,"column":11},"end":{"row":53,"column":12},"action":"insert","lines":["n"]},{"start":{"row":53,"column":12},"end":{"row":53,"column":13},"action":"insert","lines":["g"]},{"start":{"row":53,"column":13},"end":{"row":53,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":53,"column":14},"end":{"row":53,"column":16},"action":"insert","lines":["()"],"id":247}],[{"start":{"row":53,"column":15},"end":{"row":53,"column":16},"action":"insert","lines":["1"],"id":248},{"start":{"row":53,"column":16},"end":{"row":53,"column":17},"action":"insert","lines":[","]},{"start":{"row":53,"column":17},"end":{"row":53,"column":18},"action":"insert","lines":["1"]},{"start":{"row":53,"column":18},"end":{"row":53,"column":19},"action":"insert","lines":["1"]}],[{"start":{"row":53,"column":20},"end":{"row":53,"column":21},"action":"insert","lines":[":"],"id":249}],[{"start":{"row":53,"column":21},"end":{"row":54,"column":0},"action":"insert","lines":["",""],"id":250},{"start":{"row":54,"column":0},"end":{"row":54,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":54,"column":4},"end":{"row":54,"column":5},"action":"insert","lines":["i"],"id":251},{"start":{"row":54,"column":5},"end":{"row":54,"column":6},"action":"insert","lines":["f"]}],[{"start":{"row":54,"column":6},"end":{"row":54,"column":7},"action":"insert","lines":[" "],"id":252}],[{"start":{"row":54,"column":6},"end":{"row":54,"column":7},"action":"remove","lines":[" "],"id":253},{"start":{"row":54,"column":5},"end":{"row":54,"column":6},"action":"remove","lines":["f"]},{"start":{"row":54,"column":4},"end":{"row":54,"column":5},"action":"remove","lines":["i"]}],[{"start":{"row":54,"column":4},"end":{"row":54,"column":5},"action":"insert","lines":["p"],"id":254},{"start":{"row":54,"column":5},"end":{"row":54,"column":6},"action":"insert","lines":["r"]},{"start":{"row":54,"column":6},"end":{"row":54,"column":7},"action":"insert","lines":["i"]},{"start":{"row":54,"column":7},"end":{"row":54,"column":8},"action":"insert","lines":["n"]},{"start":{"row":54,"column":8},"end":{"row":54,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":54,"column":9},"end":{"row":54,"column":11},"action":"insert","lines":["()"],"id":255}],[{"start":{"row":15,"column":4},"end":{"row":16,"column":0},"action":"remove","lines":["",""],"id":256},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]},{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"remove","lines":["",""]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]},{"start":{"row":13,"column":4},"end":{"row":14,"column":0},"action":"remove","lines":["",""]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "]},{"start":{"row":12,"column":4},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "],"id":257},{"start":{"row":11,"column":54},"end":{"row":12,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":258},{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["",""]},{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""]},{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":52,"column":21},"end":{"row":53,"column":0},"action":"insert","lines":["",""],"id":259},{"start":{"row":53,"column":0},"end":{"row":53,"column":4},"action":"insert","lines":["    "]},{"start":{"row":53,"column":4},"end":{"row":53,"column":5},"action":"insert","lines":["s"]},{"start":{"row":53,"column":5},"end":{"row":53,"column":6},"action":"insert","lines":["u"]},{"start":{"row":53,"column":6},"end":{"row":53,"column":7},"action":"insert","lines":["m"]},{"start":{"row":53,"column":7},"end":{"row":53,"column":8},"action":"insert","lines":["a"]}],[{"start":{"row":53,"column":8},"end":{"row":53,"column":9},"action":"insert","lines":[" "],"id":260}],[{"start":{"row":53,"column":9},"end":{"row":53,"column":10},"action":"insert","lines":["+"],"id":261}],[{"start":{"row":53,"column":10},"end":{"row":53,"column":11},"action":"insert","lines":["="],"id":262}],[{"start":{"row":53,"column":11},"end":{"row":53,"column":12},"action":"insert","lines":[" "],"id":263}],[{"start":{"row":53,"column":12},"end":{"row":53,"column":13},"action":"insert","lines":["i"],"id":264}],[{"start":{"row":54,"column":10},"end":{"row":54,"column":11},"action":"insert","lines":["f"],"id":265}],[{"start":{"row":54,"column":11},"end":{"row":54,"column":13},"action":"insert","lines":["\"\""],"id":266}],[{"start":{"row":54,"column":12},"end":{"row":54,"column":13},"action":"insert","lines":["S"],"id":267}],[{"start":{"row":54,"column":12},"end":{"row":54,"column":13},"action":"remove","lines":["S"],"id":268}],[{"start":{"row":54,"column":12},"end":{"row":54,"column":13},"action":"insert","lines":["L"],"id":269},{"start":{"row":54,"column":13},"end":{"row":54,"column":14},"action":"insert","lines":["a"]}],[{"start":{"row":54,"column":14},"end":{"row":54,"column":15},"action":"insert","lines":[" "],"id":270},{"start":{"row":54,"column":15},"end":{"row":54,"column":16},"action":"insert","lines":["s"]},{"start":{"row":54,"column":16},"end":{"row":54,"column":17},"action":"insert","lines":["u"]},{"start":{"row":54,"column":17},"end":{"row":54,"column":18},"action":"insert","lines":["m"]},{"start":{"row":54,"column":18},"end":{"row":54,"column":19},"action":"insert","lines":["a"]},{"start":{"row":54,"column":19},"end":{"row":54,"column":20},"action":"insert","lines":["r"]}],[{"start":{"row":54,"column":19},"end":{"row":54,"column":20},"action":"remove","lines":["r"],"id":271}],[{"start":{"row":54,"column":19},"end":{"row":54,"column":20},"action":"insert","lines":[" "],"id":272},{"start":{"row":54,"column":20},"end":{"row":54,"column":21},"action":"insert","lines":["d"]},{"start":{"row":54,"column":21},"end":{"row":54,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":54,"column":22},"end":{"row":54,"column":23},"action":"insert","lines":[" "],"id":273},{"start":{"row":54,"column":23},"end":{"row":54,"column":24},"action":"insert","lines":["1"]},{"start":{"row":54,"column":24},"end":{"row":54,"column":25},"action":"insert","lines":["0"]}],[{"start":{"row":54,"column":24},"end":{"row":54,"column":25},"action":"remove","lines":["0"],"id":274},{"start":{"row":54,"column":23},"end":{"row":54,"column":24},"action":"remove","lines":["1"]},{"start":{"row":54,"column":22},"end":{"row":54,"column":23},"action":"remove","lines":[" "]},{"start":{"row":54,"column":21},"end":{"row":54,"column":22},"action":"remove","lines":["e"]}],[{"start":{"row":54,"column":21},"end":{"row":54,"column":22},"action":"insert","lines":["e"],"id":275}],[{"start":{"row":54,"column":21},"end":{"row":54,"column":22},"action":"remove","lines":["e"],"id":276},{"start":{"row":54,"column":20},"end":{"row":54,"column":21},"action":"remove","lines":["d"]},{"start":{"row":54,"column":20},"end":{"row":54,"column":21},"action":"insert","lines":["e"]},{"start":{"row":54,"column":21},"end":{"row":54,"column":22},"action":"insert","lines":["s"]},{"start":{"row":54,"column":22},"end":{"row":54,"column":23},"action":"insert","lines":[":"]}],[{"start":{"row":54,"column":23},"end":{"row":54,"column":24},"action":"insert","lines":[" "],"id":277}],[{"start":{"row":54,"column":25},"end":{"row":54,"column":26},"action":"insert","lines":[","],"id":278}],[{"start":{"row":54,"column":26},"end":{"row":54,"column":27},"action":"insert","lines":[" "],"id":279}],[{"start":{"row":54,"column":27},"end":{"row":54,"column":28},"action":"insert","lines":["s"],"id":280},{"start":{"row":54,"column":28},"end":{"row":54,"column":29},"action":"insert","lines":["u"]},{"start":{"row":54,"column":29},"end":{"row":54,"column":30},"action":"insert","lines":["m"]},{"start":{"row":54,"column":30},"end":{"row":54,"column":31},"action":"insert","lines":["a"]}],[{"start":{"row":54,"column":10},"end":{"row":54,"column":11},"action":"remove","lines":["f"],"id":281}],[{"start":{"row":54,"column":0},"end":{"row":54,"column":4},"action":"remove","lines":["    "],"id":282}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":2},"action":"insert","lines":["\"\""],"id":283}],[{"start":{"row":16,"column":2},"end":{"row":16,"column":3},"action":"insert","lines":["\""],"id":284}],[{"start":{"row":47,"column":0},"end":{"row":47,"column":2},"action":"insert","lines":["\"\""],"id":285}],[{"start":{"row":47,"column":2},"end":{"row":47,"column":3},"action":"insert","lines":["\""],"id":286}],[{"start":{"row":54,"column":0},"end":{"row":54,"column":1},"action":"insert","lines":[" "],"id":287},{"start":{"row":54,"column":1},"end":{"row":54,"column":2},"action":"insert","lines":[" "]},{"start":{"row":54,"column":2},"end":{"row":54,"column":3},"action":"insert","lines":[" "]},{"start":{"row":54,"column":3},"end":{"row":54,"column":4},"action":"insert","lines":[" "]}]]},"ace":{"folds":[],"scrolltop":572.3999999999974,"scrollleft":0,"selection":{"start":{"row":28,"column":0},"end":{"row":35,"column":22},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":25,"state":"qqstring3","mode":"ace/mode/python"}},"timestamp":1732734192121}