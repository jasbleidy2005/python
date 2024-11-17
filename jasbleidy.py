# ===========================================
# Título del trabajo: Taller de Listas en Python
# Nombre: Karen Jasbleidy Lopez Ruiz
# Fecha de creación: 11 de noviembre
# Descripción: Este archivo contiene la solución al taller de listas en Python,
# con ejercicios que cubren la creación, manipulación y métodos de listas.
# ===========================================

# 1. Crear una lista con los nombres de 5 frutas colombianas favoritas y mostrarla.
frutas = ["fresa", "papaya", "manzana", "uva", "banano"]
print("Lista de frutas:", frutas)

# 2. Acceder al segundo y cuarto elemento de la lista anterior e imprimirlos.
print("Segundo elemento:", frutas[1])
print("Cuarto elemento:", frutas[3])

# 3. Crear una lista con los números del 1 al 10 y mostrar su longitud.
numeros = list(range(1, 11))
print("Lista de números:", numeros)
print("Longitud de la lista:", len(numeros))

# 4. Concatenar las dos listas creadas en los ejercicios 1 y 3.
lista_concatenada = frutas + numeros
print("Lista concatenada:", lista_concatenada)

# 5. Modificar el tercer elemento de la lista del ejercicio 4 al valor 100.
lista_concatenada[2] = 100
print("Lista modificada:", lista_concatenada)

# 6. Borrar el último elemento de la lista del ejercicio 4.
lista_concatenada.pop()
print("Lista después de eliminar el último elemento:", lista_concatenada)

# 7. Crear una lista con 3 números enteros y multiplicar cada elemento por 5.
numeros_enteros = [2, 4, 6]
multiplicados = [x * 5 for x in numeros_enteros]
print("Lista multiplicada por 5:", multiplicados)

# 8. Crear dos listas con 5 números enteros cada una y multiplicar los elementos correspondientes de anbas listas.
lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 4, 3, 2, 1]
producto = [x * y for x, y in zip(lista1, lista2)]
print("Producto de listas:", producto)

# 9. Crear una lista de listas anidadas y acceder al segundo elemento de la segunda lista.
anidada = [[1, 2], [3, 4], [5, 6]]
print("Segundo elemento de la segunda lista:", anidada[1][1])

# 10. Crear una lista a partir de la lista del ejercicio 3, tomando los elementos del índice 2 al 6.
sublista = numeros[2:7]
print("Sublista del índice 2 al 6:", sublista)

# 11. Usar el método `.append()` para agregar un nuevo elemento al final de la lista del ejercicio 1.
frutas.append("mango")
print("Lista de frutas con nuevo elemento:", frutas)

# 12. Usar el método `.insert()` para agregar un nuevo elemento en la posición 2 de la lista del ejercicio 3.
numeros.insert(2, 100)
print("Lista de números después de insertar:", numeros)

# 13. Usar el método `.remove()` para eliminar un elemento específico de la lista del ejercicio 7.
multiplicados.remove(10)
print("Lista después de eliminar 10:", multiplicados)

# 14. Usar el método `.reverse()` para invertir el orden de la lista del ejercicio 4.
lista_concatenada.reverse()
print("Lista invertida:", lista_concatenada)

# 15. Usar el método `.sort()` para ordenar de forma ascendente la lista del ejercicio 7.
multiplicados.sort()
print("Lista ordenada:", multiplicados)

# 16. Usar el método `.pop()` para eliminar y obtener el último elemento de la lista del ejercicio 4.
ultimo = lista_concatenada.pop()
print("Último elemento eliminado:", ultimo)

# 17. Usar el método `.count()` para contar cuántas veces aparece un elemento específico en la lista del ejercicio 7.
conteo = multiplicados.count(20)
print("Cantidad de veces que aparece 20:", conteo)

# 18. Usar el método `.index()` para obtener el índice de un elemento específico en la lista del ejercicio 4.
indice = lista_concatenada.index(100)
print("Índice del elemento 100:", indice)

# 19. Usar el método `.clear()` para eliminar todos los elementos de la lista del ejercicio 1.
frutas.clear()
print("Lista de frutas después de limpiar:", frutas)

# 20. Crear una lista vacía y utilizar un bucle `for` para agregar los números del 1 al 10.
lista_vacia = []
for i in range(1, 11):
    lista_vacia.append(i)
print("Lista llena usando bucle for:", lista_vacia)

# 21. Crear una lista de números enteros y utilizar un bucle `while` para eliminar los elementos impares.
numeros_enteros = list(range(1, 11))
i = 0
while i < len(numeros_enteros):
    if numeros_enteros[i] % 2 != 0:
        numeros_enteros.pop(i)
    else:
        i += 1
print("Lista después de eliminar impares:", numeros_enteros)

# 22. Crear una lista con los nombres de 5 materias favoritas y ordenarlas alfabéticamente.
materias = ["Matemáticas", "Calculo", "Física", "Ingles", "Programación"]
materias.sort()
print(materias)

# 23. Crear una lista con los números del 1 al 15 y mostrar solo los múltiplos de 3.
numeros = list(range(1, 16))
multiplos_de_3 = [num for num in numeros if num % 3 == 0]
print(multiplos_de_3)

# 24. Crear una lista con los nombres de 10 artistas favoritos y utilizar un bucle `for` para imprimir cada nombre en mayúsculas.
artistas = ["Adele", "Tokio hotel", "Arctic monkeys", "EN8T", "Oasis", "Ed Sheeran", "Don omar", "Bruno Mars", "canservero", "Tom odell"]
for artista in artistas:
    print(artista.upper())


# 25. Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con solo los números pares.
numeros = list(range(1, 21))
pares = [num for num in numeros if num % 2 == 0]
print(pares)

# 26. Crear una lista con los nombres de los municipios del departamento de Arauca y utilizar un bucle `for` para imprimir cada nombre en orden inverso.
municipios = ["Arauca", "Arauquita", "Saravena", "Fortul", "Tame", "Puerto Rondón", "Cravo Norte"]
for municipio in municipios[::-1]:
    print(municipio)


# 27. Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de cada número.
numeros = list(range(1, 13))
cuadrados = [num ** 2 for num in numeros]
print(cuadrados)

# 28. Crear una lista con los meses del año y utilizar el método `.index()` para obtener el índice del mes "Junio".
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
indice_junio = meses.index("Junio")
print(indice_junio)

# 29. Crear una lista con los nombres que usted le pondría a 6 mascotas y utilizar el método `.remove()` para eliminar una mascota de la lista.
mascotas = ["Mia", "Emma", "Douglas", "Alaska", "Adele", "Oreo"]
mascotas.remove("Adele")
print(mascotas)

# 30. Crear una lista con los números del 1 al 20 y utilizar el método `.sort(reverse=True)` para ordenarla de forma descendente.
numeros = list(range(1, 21))
numeros.sort(reverse=True)
print(numeros)

# 31. Crear una lista con los nombres de 4 libros favoritos y utilizar el método `.append()` para agregar un nuevo libro al final de la lista.
libros = ["Lujuria", "Orgullo y prejuicio", "Antes de diciembre", "Boulevard"]
libros.append("Damian")
print(libros)


# 32. Crear una lista con los números del 1 al 15 y utilizar una comprensión de listas para crear una nueva lista con los números impares.
numeros = list(range(1, 16))
impares = [num for num in numeros if num % 2 != 0]
print(impares)


# 33. Crear una lista con los nombres de 7 comidas favoritas y utilizar el método `.insert()` para agregar una nueva comida en la posición 3.
comidas = ["Bandeja paisa", "Arroz con huevo", "Ensalada roja", "Sopera", "Sudado de pollo", "Pollo apanado", "Empanadas"]
comidas.insert(2, "Pizza")
print(comidas)

# 34. Crear una lista con los números del 1 al 10 y utilizar el método `.extend()` para agregar una segunda lista con los números del 11 al 15.
numeros = list(range(1, 11))
numeros.extend(list(range(11, 16)))
print(numeros)

# 35. Crear una lista con los nombres de 6 compañeros y utilizar el método `.count()` para contar cuántas veces aparece un nombre específico en la lista.
compañeros = ["Jan", "Sebastian", "Jan", "Samuel", "Santiago", "Jasbleidy"]
conteo = compañeros.count("Jan")
print(conteo)

# 36. Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los números divisibles por 3.
numeros = list(range(1, 13))
divisibles_por_3 = [num for num in numeros if num % 3 == 0]
print(divisibles_por_3)

# 37. Crear una lista con los nombres de 5 artistas musicales favoritos y utilizar el método `.reverse()` para invertir el orden de la lista.
artistas = ["CNCO", "Tom Kaulitz", "RBD", "Babi", "Nanpa"]
artistas.reverse()
print(artistas)

# 38. Crear una lista con los números del 1 al 20 y utilizar una función lambda y el método `.sort()` para ordenar la lista de forma descendente.
numeros = list(range(1, 21))
numeros.sort(key=lambda x: -x)
print(numeros)

# 39. Crear una lista con las materias de la universidad y utilizar el método `.pop()` para eliminar y obtener el último elemento de la lista.
materias = ["Matemáticas", "Física", "Fundamentos de Electronica", "Formulacion de proyectos", "Programación"]
ultima_materia = materias.pop()
print(ultima_materia)

# 40. Crear una lista con los números del 1 al 25 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 5.
numeros = list(range(1, 26))
multiplos_de_5 = [num for num in numeros if num % 5 == 0]
print(multiplos_de_5)


# 41. Crear una lista con los nombres de 8 deportes y utilizar una función anónima y el método `.sort()` para ordenar la lista.
deportes = ["Fútbol", "Baloncesto", "Natación", "Tenis", "Voleibol", "Atletismo", "Golf", "Boxeo"]
deportes.sort(key=lambda x: x)
print(deportes)

# 42. Crear una lista con los números del 1 al 15 y utilizar el método `.clear()` para eliminar todos los elementos de la lista.
numeros = list(range(1, 16))
numeros.clear()
print(numeros)

# 43. Crear una lista con los nombres de 6 países y utilizar un bucle `for` para imprimir cada nombre en minúsculas.
paises = ["Arrmenia", "Alemania", "Suiza", "Corea", "Israel", "Tailandia"]
for pais in paises:
    print(pais.lower())


# 44. Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de los números pares.
numeros = list(range(1, 21))
cuadrados_pares = [num ** 2 for num in numeros if num % 2 == 0]
print(cuadrados_pares)


# 45. Crear una lista con los nombres de 10 videojuegos y utilizar el método `.index()` para obtener el índice de un juego específico.
videojuegos = ["The Legend of Zelda", "Super Mario", "Minecraft", "Fortnite", "Call of Duty", "GTA V", "Among Us", "Halo", "FIFA", "Overwatch"]
indice_minecraft = videojuegos.index("Minecraft")
print(indice_minecraft)


# 46. Crear una lista con los números del 1 al 12 y utilizar el método `.remove()` para eliminar un número específico de la lista.
numeros = list(range(1, 13))
numeros.remove(5)
print(numeros)

# 47. Crear una lista con los nombres de 7 monumentos colombianos y utilizar una función lambda y el método `.sort(key=len)` para ordenar la lista por longitud de nombre.
monumentos = ["Catedral de Sal", "La Popa", "Monserrate", "Castillo de San Felipe", "Puente de Boyacá", "Cañón del Chicamocha", "El Peñol"]
monumentos.sort(key=lambda x: len(x))
print(monumentos)

# 48. Crear una lista con los números del 1 al 18 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 3 y 5.
numeros = list(range(1, 19))
multiplos_3_y_5 = [num for num in numeros if num % 3 == 0 and num % 5 == 0]
print(multiplos_3_y_5)

# 49. Crear una lista con los nombres de 6 asignaturas que le parecen interesantes de la carrera y utilizar el método `.append()` para agregar un nuevo nombre al final de la lista.
asignaturas = ["Programación II", "Bases de Datos", "Metodologia de desarrollo I", "Ingeniería de Software I", "Estadistica", "Formacion de instructores"]
asignaturas.append("Fisica de electricidad")
print(asignaturas)


# 50. Crear una lista con los números del 1 al 25 y utilizar el método `.pop()` para eliminar y obtener el elemento de la posición 7.
numeros = list(range(1, 26))
elemento_pop = numeros.pop(7)
print(elemento_pop)
print(numeros)
