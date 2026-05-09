# COMENTARIOS EN PYTHON
# Este es un comentario, no se ejecuta
# En Python, cualquier línea que comience con # es un comentario
# Los comentarios son notas para entender el código

# print ("Hola Mundo, desde Python")  # Esta línea comentada no se ejecuta

# COMENTARIOS DE VARIAS LÍNEAS
"""
Este es un comentario de varias líneas, no se ejecuta
Se usa con triple comillas (\"\"\"...\"\"\") para escribir comentarios más largos
Útil para explicar secciones completas de código
"""

# ----------------------------------------------------------
# ¿QUÉ ES UNA VARIABLE?
# ----------------------------------------------------------
# Una variable es un "contenedor" donde guardamos información
# Tiene un nombre y un valor
# Sintaxis: <nombre_variable> = <valor>

"""
-------------------------------------
<variable> = <valor de la variable>
-------------------------------------
"""

# Ejemplo básico (comentado para no ejecutar):
# first_name = "Juan"          # string (texto)
# age = 30                      # int (número entero)
# print(first_name + " tiene " + str(age) + " años")
# # ↑ Concatenamos strings. str() convierte el int a string

# print(type(first_name))       # <class 'str'>
# print(type(age))              # <class 'int'>

# ----------------------------------------------------------
# CARACTERÍSTICAS ESPECIALES DE PYTHON
# ----------------------------------------------------------

# Python es TIPADO DINÁMICO
# No necesitas declarar qué tipo es la variable
# Python lo entiende automáticamente por el valor que le asignas

# Ejemplo:
#   nombre = "Juan"     # Python ve comillas → lo trata como string
#   edad = 30           # Python ve un número → lo trata como int
#   altura = 1.75       # Python ve un decimal → lo trata como float

# CONVENCIÓN snake_case
# En Python se recomienda usar snake_case para nombrar variables:
# - Palabras separadas con guiones bajos, en minúsculas
# ✓ Correcto: first_name, user_age, total_price
# ✗ Incorrecto: firstName (esto es camelCase, de otros lenguajes)

# ----------------------------------------------------------
# TIPOS DE DATOS PRINCIPALES EN PYTHON
# ----------------------------------------------------------

# 1. STRING (Texto)
#    Se escribe entre comillas simples '' o dobles ""
#    Ejemplo: nombres, mensajes, frases

# 2. INTEGER (Números enteros)
#    Números sin decimales: 1, 2, -5, 1000, etc.

# 3. FLOAT (Números decimales)
#    Números con punto decimal: 3.14, 9.8, -2.5, etc.

# 4. BOOLEAN (Verdadero o Falso)
#    Solo tiene dos valores: True (verdadero) o False (falso)


# ----------------------------------------------------------
# STRING (Texto)
# ----------------------------------------------------------
# Se escribe entre comillas simples '' o dobles ""
# Ejemplo: nombres, mensajes, frases, cualquier texto

first_name = "Cody"      # Guardamos el texto "Cody" en una variable
last_name = 'Facilito'   # Ambas formas () y ("") son válidas

print(first_name)        # Imprime: Cody
print(last_name)         # Imprime: Facilito

print(type(first_name))  # Imprime: <class 'str'>
# ↑ type() nos muestra qué tipo de dato es la variable
print(type(last_name))   # Imprime: <class 'str'>


# ----------------------------------------------------------
# INTEGER (Números enteros)
# ----------------------------------------------------------
# Números sin decimales: 1, 2, -5, 1000, etc.
# Se pueden usar guiones bajos para legibilidad (1_000_000 = 1000000)

age = 25                 # Un número entero
number = 100_000_000     # Mil millones, separado con _ para legibilidad
# Nota: Los guiones bajos NO afectan el valor, solo mejoran la lectura

print(number)            # Imprime: 100000000
print(type(number))      # Imprime: <class 'int'>
print(age)               # Imprime: 25
print(type(age))         # Imprime: <class 'int'>


# ----------------------------------------------------------
# FLOAT (Números decimales)
# ----------------------------------------------------------
# Números con punto decimal: 3.14, 9.8, -2.5, etc.

pi = 3.1416              # Número con decimales (constante matemática)

print(pi)                # Imprime: 3.1416
print(type(pi))          # Imprime: <class 'float'>


# ----------------------------------------------------------
# BOOLEAN (Verdadero o Falso)
# ----------------------------------------------------------
# Solo tiene dos valores: True (verdadero) o False (falso)
# Útil para tomar decisiones en el código

is_active = True         # Esta variable es verdadera
is_admin = False         # Esta variable es falsa

print(is_active)         # Imprime: True
print(is_admin)          # Imprime: False
print(type(is_active))   # Imprime: <class 'bool'>
print(type(is_admin))    # Imprime: <class 'bool'>


# ----------------------------------------------------------
# CONSTANTES EN PYTHON
# ----------------------------------------------------------
# Python no tiene "constantes" reales, pero por CONVENCIÓN,
# si una variable debe ser constante (no cambiar), se escribe en MAYÚSCULAS
# La idea es comunicar: "Esta variable no debe cambiar"

PI = 3.1416              # Constante (se escribe en mayúsculas)
GRAVITY = 9.81           # Constante gravitacional

# ⚠️ Nota importante:
# Python permite cambiar el valor, pero NO SE DEBE HACER:
PI = 3.1592  # ❌ Aunque funciona, no es recomendable. Causa confusión

print(PI)                # Imprime: 3.1592 (cambió, pero no es lo correcto)
print(GRAVITY)           # Imprime: 9.81
print(type(PI))          # Imprime: <class 'float'>
print(type(GRAVITY))     # Imprime: <class 'float'>