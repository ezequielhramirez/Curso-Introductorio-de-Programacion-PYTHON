# SOLICITAR VALORES POR TECLADO
# La función input() permite que el usuario escriba datos en el programa

# ----------------------------------------------------------
# FUNCIÓN input()
# ----------------------------------------------------------
# Sintaxis: variable = input("mensaje para el usuario")
#
# - Muestra un mensaje en la pantalla
# - Espera a que el usuario escriba algo y presione Enter
# - Guarda lo que escribió en la variable
# ⚠️ IMPORTANTE: input() SIEMPRE devuelve un STRING (texto)

# Ejemplo simple:
# full_name = input("Ingrese su nombre completo: ")
# print("El nombre ingresado es: ", full_name)

# ----------------------------------------------------------
# CONVERSIÓN DE TIPOS (type casting)
# ----------------------------------------------------------
# Aunque input() siempre devuelve texto, a veces necesitamos números
# DEBEMOS CONVERTIR el texto a otro tipo de dato

# Conversión a STRING (texto)
# str() asegura que es un string (aunque input() ya lo es)
first_name = str(input("Ingrese su nombre: "))
# Ejemplo: El usuario escribe "Juan" → Se guarda como "Juan"
print("✓ Nombre guardado como STRING")

# Conversión a INTEGER (número entero)
# int() convierte el texto a un número entero
# Nota: Si el usuario escribe "veinticinco", esto va a FALLAR
# Solo funciona con dígitos: "25" → 25
age = int(input("Ingrese su edad: "))
# Ejemplo: El usuario escribe "25" → Se convierte al número 25
print("✓ Edad guardada como INTEGER")

# Conversión a FLOAT (número decimal)
# float() convierte el texto a un número con decimales
altura = float(input("Ingrese su altura (en metros): "))
# Ejemplo: El usuario escribe "1.75" → Se convierte al número 1.75
print("✓ Altura guardada como FLOAT")

# Conversión a BOOLEAN (verdadero/falso)
# Se usa una comparación que devuelve True o False
# Ejemplo: si el usuario escribe "yes", la comparación es True
# Si escribe cualquier otra cosa, la comparación es False
status = bool(input("¿Tu usuario se encuentra activo? (yes / no): ") == "yes")
# El usuario escribe "yes" → Comparación es True → Se guarda True
print("✓ Estado guardado como BOOLEAN")

# ----------------------------------------------------------
# CONVERSIÓN SIN input()
# ----------------------------------------------------------
# También se puede convertir variables que ya existen

number = str(10)  # Convierte el número 10 al texto "10"
print("\nConversión de número a string:")
print("El numero es: ", number)
print("Tipo:", type(number))  # Imprime: <class 'str'>

# ----------------------------------------------------------
# RESUMEN DE LO INGRESADO
# ----------------------------------------------------------

print("\n--- RESUMEN DE DATOS INGRESADOS ---")
print("El nombre ingresado es: ", first_name)    # Imprime el texto
print("  Tipo:", type(first_name))               # Imprime: <class 'str'>

print("La edad ingresada es: ", age)             # Imprime el número
print("  Tipo:", type(age))                      # Imprime: <class 'int'>

print("La altura ingresada es: ", altura)        # Imprime el decimal
print("  Tipo:", type(altura))                   # Imprime: <class 'float'>

print("El estado del usuario es: ", status)      # Imprime True o False
print("  Tipo:", type(status))                   # Imprime: <class 'bool'>

# ----------------------------------------------------------
# TABLA DE CONVERSIONES
# ----------------------------------------------------------
"""
str()   → Convierte a STRING (texto)
int()   → Convierte a INTEGER (número entero)
float() → Convierte a FLOAT (número decimal)
bool()  → Convierte a BOOLEAN (True/False)
""" 




