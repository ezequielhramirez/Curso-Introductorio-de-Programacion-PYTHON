# SLICING (Rebanado de listas)
# El slicing permite extraer una "rebanada" de una lista
# Sintaxis: lista[inicio:fin:paso]

# ----------------------------------------------------------
# VISUALIZACIÓN DE ÍNDICES
# ----------------------------------------------------------
# Índices positivos (desde el inicio):
#        0    1         2          3    4      5      6
#     ["Python", "Java", "JavaScript", "C#", "Ruby", "Go", "Swift"]
#
# Índices negativos (desde el final):
#       -7   -6        -5         -4   -3     -2     -1
#     ["Python", "Java", "JavaScript", "C#", "Ruby", "Go", "Swift"]
#
# Los índices negativos permiten acceder desde el final sin contar elementos

cursos = ["Python", "Java", "JavaScript", "C#", "Ruby", "Go", "Swift"]

# ----------------------------------------------------------
# SLICING BÁSICO: [inicio:fin]
# ----------------------------------------------------------
# Devuelve elementos DESDE 'inicio' HASTA 'fin' (sin incluir fin)

# Desde el índice 1 hasta el 3 (sin incluir el 3)
# Índices: 1="Java", 2="JavaScript"
sublista1 = cursos[1:3]
print("cursos[1:3]:")
print(sublista1)  # Imprime: ['Java', 'JavaScript']

# Del inicio hasta el índice 2 (sin incluir el 2)
# Índices: 0="Python", 1="Java"
inicio = cursos[:2]
print("\ncursos[:2]:")
print(inicio)     # Imprime: ['Python', 'Java']

# Desde el índice 2 hasta el final
# Índices: 2, 3, 4, 5, 6
fin = cursos[2:]
print("\ncursos[2:]:")
print(fin)        # Imprime: ['JavaScript', 'C#', 'Ruby', 'Go', 'Swift']

# ----------------------------------------------------------
# SLICING COMPLETO: [:]
# ----------------------------------------------------------
# Desde el inicio hasta el final (copia completa)

copia_completa = cursos[:]
print("\ncursos[:]  (copia completa):")
print(copia_completa)
# Imprime: ['Python', 'Java', 'JavaScript', 'C#', 'Ruby', 'Go', 'Swift']

# ----------------------------------------------------------
# SLICING CON PASO: [inicio:fin:paso]
# ----------------------------------------------------------
# El "paso" determina la frecuencia de elementos
# paso=1: cada elemento (por defecto)
# paso=2: cada 2 elementos (uno sí, uno no)
# paso=-1: del revés

# Desde índice 1 al 7, con paso 2 (uno sí, uno no)
# Toma elementos en las posiciones 1, 3, 5
cursos_copy = cursos[1::2]
print("\ncursos[1::2]  (desde el 1, cada 2 elementos):")
print(cursos_copy)
# Imprime: ['Java', 'C#', 'Go']

# Otro ejemplo: desde 0 al final, con paso 2
# Toma elementos en posiciones 0, 2, 4, 6
print("\ncursos[::2]  (desde el inicio, cada 2 elementos):")
print(cursos[::2])
# Imprime: ['Python', 'JavaScript', 'Ruby', 'Swift']

# ----------------------------------------------------------
# SLICING INVERSO: [::-1]
# ----------------------------------------------------------
# Devuelve la lista AL REVÉS
# paso=-1 significa "en dirección inversa"

cursos_inversa = cursos[::-1]
print("\ncursos[::-1]  (lista invertida):")
print(cursos_inversa)
# Imprime: ['Swift', 'Go', 'Ruby', 'C#', 'JavaScript', 'Java', 'Python']

# ----------------------------------------------------------
# NOTA IMPORTANTE: SHALLOW COPY (Copia superficial)
# ----------------------------------------------------------
# Cuando usamos slicing para crear una copia, se crea una NUEVA lista
# Modificar la nueva lista NO afecta la lista original
# (porque son dos objetos diferentes en memoria)

print("\n--- SHALLOW COPY (Copia independiente) ---")
original = [1, 2, 3, 4, 5]
copia = original[:]  # Crear copia con slicing

# Modificar la copia
copia[0] = 999

print("Lista original:", original)  # [1, 2, 3, 4, 5] - SIN cambios
print("Copia modificada:", copia)   # [999, 2, 3, 4, 5] - SOLO la copia cambió

# Esto también se puede hacer con:
# copia2 = original.copy()    # Método copy()
# copia3 = list(original)     # Convertir a list()

# Pero SIN copiar, tendríamos:
print("\n--- SIN COPIAR (referencia) ---")
lista_a = [1, 2, 3]
lista_b = lista_a    # Ahora lista_b apunta a lista_a

lista_b[0] = 999
print("Lista A:", lista_a)  # [999, 2, 3] - ¡Cambió también!
print("Lista B:", lista_b)  # [999, 2, 3] - Son la misma lista

# ⚠️ Por eso siempre COPIAR si no quieres que cambien ambas

