"""listas.py

¿QUÉ ES UNA LISTA?
Una lista es una COLECCIÓN ORDENADA y MODIFICABLE de elementos.

CARACTERÍSTICAS:
- Se define con corchetes []
- Puede contener cualquier tipo de dato (números, textos, booleanos, etc.)
- Incluso puede contener otras listas
- Es MODIFICABLE: se pueden agregar, eliminar o cambiar elementos
- Los elementos están EN ORDEN y se acceden por su POSICIÓN (índice)
- El primer elemento está en posición 0 (no 1)

ÍNDICES:
- Positivos: 0, 1, 2, 3... (desde el inicio)
- Negativos: -1, -2, -3... (desde el final)

OPERACIONES PRINCIPALES:
1. Crear listas
2. Acceder a elementos
3. Modificar elementos
4. Agregar elementos (append, insert, extend)
5. Eliminar elementos (remove, pop, clear)
6. Búsqueda (index, count)
7. Ordenar y copiar (sort, reverse, copy)
8. Recorrer listas (for loops)
9. Slicing (rebanado)
10. List comprehensions (avanzado)

"""

# ==============================================================
# 1. CREAR LISTAS
# ==============================================================

# Lista vacía
vacia = []
print("Lista vacía:", vacia)

# Lista con números
numeros = [1, 2, 3, 4]
print("Lista de números:", numeros)

# Lista con diferentes tipos de datos
mezclada = [1, 'dos', 3.0, True]
# ↑ Número, Texto, Decimal, Booleano: ¡todo en una lista!
print("Lista mezclada:", mezclada)

# Lista de cursos
cursos = ["Python", "Java", "JavaScript", "C#", "Ruby"]
print("Cursos:", cursos)

# ==============================================================
# 2. ACCEDER A ELEMENTOS - ÍNDICES
# ==============================================================

print("\n--- ACCESO A ELEMENTOS ---")

#        0    1         2          3    4
#     ["Python", "Java", "JavaScript", "C#", "Ruby"]
#
#       -5   -4        -3         -2   -1

# Acceder al PRIMER elemento (índice 0)
primer = cursos[0]
print("Primer elemento (índice 0):", primer)  # Python

# Acceder al TERCER elemento (índice 2)
tercero = cursos[2]
print("Tercer elemento (índice 2):", tercero)  # JavaScript

# Acceder al ÚLTIMO elemento (índice -1)
ultimo = cursos[-1]
print("Último elemento (índice -1):", ultimo)  # Ruby

# Acceder al TERCERO DESDE EL FINAL (índice -3)
tercero_final = cursos[-3]
print("Tercero desde el final (índice -3):", tercero_final)  # JavaScript

# ==============================================================
# 3. MODIFICAR ELEMENTOS
# ==============================================================

print("\n--- MODIFICAR ELEMENTOS ---")

numeros = [1, 2, 3, 4]
print("Antes:", numeros)

numeros[1] = 20  # Cambiamos el elemento en índice 1 (el 2)
print("Después de cambiar índice 1:", numeros)  # [1, 20, 3, 4]

cursos = ["Python", "Java", "JavaScript", "C#", "Ruby"]
cursos[2] = "C++"  # Cambiar el tercer elemento
print("Después de cambiar 'JavaScript' a 'C++':", cursos)

cursos[1] = "PHP"  # Cambiar el segundo elemento
print("Después de cambiar 'Java' a 'PHP':", cursos)

# ==============================================================
# 4. OBTENER INFORMACIÓN DE LA LISTA
# ==============================================================

print("\n--- INFORMACIÓN DE LA LISTA ---")

cursos = ["Python", "Java", "JavaScript", "C#", "Ruby"]

# len() - LONGITUD (cuántos elementos hay)
longitud = len(cursos)
print("Cantidad de elementos:", longitud)  # 5

# Acceder al último elemento usando len()
valor = cursos[len(cursos) - 1]
print("Último elemento usando len():", valor)  # Ruby
# len(cursos) = 5, entonces 5-1 = 4, y cursos[4] = "Ruby"

# count() - CONTAR cuántas veces aparece un elemento
cursos_con_repetidos = ["Python", "Java", "Python", "C#", "Python"]
cantidad = cursos_con_repetidos.count("Python")
print("¿Cuántas veces aparece 'Python'?", cantidad)  # 3

# index() - ENCONTRAR la posición de un elemento
cursos = ["Python", "Java", "JavaScript", "C#", "Ruby"]
posicion = cursos.index("C#")
print("¿Dónde está 'C#'?", posicion)  # 3 (está en índice 3)

# ==============================================================
# 5. SLICING (Rebanado)
# ==============================================================

print("\n--- SLICING (Rebanado) ---")

cursos = ["Python", "Java", "JavaScript", "C#", "Ruby"]

# Desde índice 1 hasta 3 (sin incluir 3)
sublista = cursos[1:3]
print("cursos[1:3]:", sublista)  # ['Java', 'JavaScript']

# Desde el inicio hasta índice 2
inicio = cursos[:2]
print("cursos[:2]:", inicio)  # ['Python', 'Java']

# Desde índice 2 hasta el final
fin = cursos[2:]
print("cursos[2:]:", fin)  # ['JavaScript', 'C#', 'Ruby']

# Copia completa
copia = cursos[:]
print("cursos[:] (copia):", copia)

# Con paso (cada 2 elementos)
cada_dos = cursos[::2]
print("cursos[::2] (cada 2):", cada_dos)  # ['Python', 'JavaScript', 'Ruby']

# Invertida
invertida = cursos[::-1]
print("cursos[::-1] (invertida):", invertida)

# ==============================================================
# 6. RECORRER UNA LISTA (for loop)
# ==============================================================

print("\n--- RECORRER LISTA ---")

cursos = ["Python", "Java", "JavaScript"]

# For simple
print("For simple:")
for curso in cursos:
    print("-", curso)

# Con índice (enumerate)
print("\nCon índice (enumerate):")
for indice, curso in enumerate(cursos):
    print(f"Posición {indice}: {curso}")

# ==============================================================
# 7. LIST COMPREHENSION (avanzado)
# ==============================================================

print("\n--- LIST COMPREHENSION ---")

# Crear lista de cuadrados
cuadrados = [x*x for x in range(6)]
print("Cuadrados del 0 al 5:", cuadrados)  # [0, 1, 4, 9, 16, 25]

# Crear lista de números pares
pares = [x for x in range(10) if x % 2 == 0]
print("Números pares del 0 al 9:", pares)  # [0, 2, 4, 6, 8]

# ==============================================================
# 8. LISTA DE LISTAS (Matriz simple)
# ==============================================================

print("\n--- LISTA DE LISTAS (Matriz) ---")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#  fila 0, fila 1, fila 2

print("Matriz:")
for fila in matriz:
    print(fila)

# Acceder a un elemento específico
elemento = matriz[1][2]  # Fila 1, columna 2
print(f"\nElemento en fila 1, columna 2: {elemento}")  # 6

# ==============================================================
# 9. LISTA MIXTA
# ==============================================================

print("\n--- LISTA MIXTA ---")

my_list = ["String", 123, 45.67, True, [1, 2, 3]]
# Una lista que contiene diferentes tipos de datos incluyendo otra lista

print("Mi lista es:", my_list)
print("Tipo:", type(my_list))  # <class 'list'>

# ==============================================================
# 10. FORMATEO Y PRESENTACIÓN
# ==============================================================

print("\n--- FORMATEO DIDÁCTICO ---")

# Lista bien formateada (más legible)
my_courses = [
    "Python",
    "Java",
    "JavaScript"
]
print("Cursos:", my_courses)

my_numbers = [
    1,
    2,
    3,
    4,
    5
]
print("Números:", my_numbers)

# ==============================================================
# RESUMEN DE MÉTODOS PRINCIPALES
# ==============================================================

"""
MÉTODOS DE LISTAS:

append(x)       → Añade x al final
extend(iterable) → Añade todos los elementos de un iterable
insert(i, x)    → Inserta x en la posición i
remove(x)       → Elimina la primera ocurrencia de x
pop(i)          → Quita y devuelve el elemento en i (por defecto el último)
clear()         → Vacía la lista
index(x)        → Devuelve el índice de la primera ocurrencia de x
count(x)        → Cuenta cuántas veces aparece x
sort()          → Ordena la lista (modifica la original)
reverse()       → Invierte el orden de la lista
copy()          → Devuelve una copia superficial de la lista
len(lista)      → Devuelve la cantidad de elementos

FUNCIONES ÚTILES:
len(lista)      → Longitud
min(lista)      → Valor mínimo (si contiene números)
max(lista)      → Valor máximo (si contiene números)
sum(lista)      → Suma total (si contiene números)
sorted(lista)   → Devuelve una nueva lista ordenada
"""



