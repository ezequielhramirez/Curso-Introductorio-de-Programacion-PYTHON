# INDICADORES DE POSICIÓN EN LISTAS
# 
# Índices positivos (desde el inicio):
#        0    1         2          3    4      5      6
#     ["Python", "Java", "JavaScript", "C#", "Ruby", "Go", "Swift"]
#
# Índices negativos (desde el final):
#       -7   -6        -5         -4   -3     -2     -1
#     ["Python", "Java", "JavaScript", "C#", "Ruby", "Go", "Swift"]
#
# Esta guía visual ayuda a entender las posiciones en una lista

cursos = ["Python", "Java", "JavaScript", "C#", "Ruby", "Go", "Swift"]

# ==============================================================
# MÉTODO append() - AGREGAR UN ELEMENTO AL FINAL
# ==============================================================
# Sintaxis: lista.append(elemento)
# - Agrega UN elemento al final de la lista
# - MODIFICA la lista original
# - Devuelve None (no devuelve nada)

print("--- MÉTODO append() ---")
print("Lista original:", cursos)

cursos.append("Kotlin")  # Agregamos "Kotlin" al final
print("Después de append('Kotlin'):", cursos)

print("Número de elementos en la lista:", len(cursos))
# ↑ len() devuelve cuántos elementos hay

# ==============================================================
# MÉTODO insert() - INSERTAR EN UNA POSICIÓN ESPECÍFICA
# ==============================================================
# Sintaxis: lista.insert(posición, elemento)
# - Agrega un elemento en una posición específica
# - Los elementos posteriores se "corren" hacia la derecha
# - MODIFICA la lista original

print("\n--- MÉTODO insert() ---")
print("Lista antes de insert():", cursos)

cursos.insert(0, "C++")  # Insertamos "C++" en la posición 0 (al inicio)
print("Después de insert(0, 'C++'):", cursos)
# Nota: "Python" que estaba en posición 0, ahora está en posición 1
# Nota: "Kotlin" que estaba al final, sigue al final

# ==============================================================
# MÉTODO extend() - AGREGAR VARIOS ELEMENTOS
# ==============================================================
# Sintaxis: lista.extend(otra_lista)
# - Agrega TODOS los elementos de otra lista
# - Los elementos se agregan al final, uno por uno
# - MODIFICA la lista original

print("\n--- MÉTODO extend() ---")
print("Lista antes de extend():", cursos)

new_courses = ["PHP", "TypeScript"]  # Una nueva lista con 2 elementos
cursos.extend(new_courses)  # Agregamos todos estos elementos
print("Después de extend(['PHP', 'TypeScript']):", cursos)

# ==============================================================
# DIFERENCIA IMPORTANTE: append() vs extend()
# ==============================================================

print("\n--- DIFERENCIA: append() vs extend() ---")

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

print("\nLista 1 original:", lista1)
print("Lista 2 original:", lista2)

# append(): Agrega la LISTA COMPLETA como UN elemento
lista1.append([4, 5])
print("Después de append([4, 5]):", lista1)
# ↑ La lista ahora tiene un elemento que es otra lista
# Resultado: [1, 2, 3, [4, 5]]

# extend(): Agrega CADA ELEMENTO por separado
lista2.extend([4, 5])
print("Después de extend([4, 5]):", lista2)
# ↑ Cada número se agrega individualmente
# Resultado: [1, 2, 3, 4, 5]

# ==============================================================
# OTROS MÉTODOS IMPORTANTES (referencia rápida)
# ==============================================================

print("\n--- OTROS MÉTODOS ÚTILES ---")

# remove() - Elimina la PRIMERA ocurrencia de un elemento
lista = [1, 2, 3, 2, 4]
print("\nLista:", lista)
lista.remove(2)  # Elimina el primer 2 que encuentra
print("Después de remove(2):", lista)  # [1, 3, 2, 4]

# pop() - Elimina y DEVUELVE el elemento en una posición
lista = [1, 2, 3, 4]
print("\nLista:", lista)
ultimo = lista.pop()  # Elimina y guarda el último elemento (4)
print("Elemento eliminado con pop():", ultimo)  # 4
print("Lista después de pop():", lista)  # [1, 2, 3]

# pop(posición) - Elimina en una posición específica
lista = [1, 2, 3, 4]
print("\nLista:", lista)
segundo = lista.pop(1)  # Elimina y guarda el elemento en índice 1 (el 2)
print("Elemento eliminado con pop(1):", segundo)  # 2
print("Lista después de pop(1):", lista)  # [1, 3, 4]

# clear() - Vacía toda la lista
lista = [1, 2, 3]
print("\nLista:", lista)
lista.clear()
print("Después de clear():", lista)  # []

# sort() - Ordena la lista (MODIFICA la original)
numeros = [3, 1, 4, 1, 5, 9]
print("\nNúmeros:", numeros)
numeros.sort()
print("Después de sort():", numeros)  # [1, 1, 3, 4, 5, 9]

# reverse() - Invierte el orden
numeros = [1, 2, 3, 4]
print("\nNúmeros:", numeros)
numeros.reverse()
print("Después de reverse():", numeros)  # [4, 3, 2, 1]

# copy() - Crea una copia independiente
original = [1, 2, 3]
copia = original.copy()
copia[0] = 999
print("\nOriginal:", original)  # [1, 2, 3] - sin cambios
print("Copia modificada:", copia)  # [999, 2, 3] - solo cambió la copia

# index() - Encuentra la posición de un elemento
numeros = [10, 20, 30, 40]
pos = numeros.index(30)  # ¿Dónde está el 30?
print("\nLista:", numeros)
print("Posición de 30:", pos)  # 2

# count() - Cuenta cuántas veces aparece un elemento
numeros = [1, 2, 2, 3, 2, 4]
cantidad = numeros.count(2)  # ¿Cuántos 2 hay?
print("Lista:", numeros)
print("Cantidad de 2:", cantidad)  # 3



