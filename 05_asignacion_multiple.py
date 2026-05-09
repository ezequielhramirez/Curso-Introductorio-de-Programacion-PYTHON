# ASIGNACIÓN DE MÚLTIPLES VARIABLES EN UNA SOLA LÍNEA
# Python permite asignar varios valores a varias variables de una sola vez

# ----------------------------------------------------------
# SINTAXIS
# ----------------------------------------------------------
# variable1, variable2, variable3 = valor1, valor2, valor3
# 
# El orden es IMPORTANTE:
# - Primer valor → Primera variable
# - Segundo valor → Segunda variable
# - Tercer valor → Tercera variable

# ----------------------------------------------------------
# EJEMPLO BÁSICO
# ----------------------------------------------------------

name, surname, age = "Juan", "Perez", 30
#     |         |         |       |      |
#     |         |         |       |      └─ Se asigna a 'age'
#     |         |         |       └─────── Se asigna a 'surname'
#     |         |         └────────────── Se asigna a 'name'
#     └─────────────────────────────────── Primer valor

# Verificamos que se asignaron correctamente
print("El nombre es: ", name)      # Imprime: Juan
print("El apellido es: ", surname) # Imprime: Perez
print("La edad es: ", age)         # Imprime: 30

# Concatenamos los valores
print("El nombre es: ", name + " " + surname + " y su edad es: ", age)
# Imprime: El nombre es: Juan Perez y su edad es: 30

# ----------------------------------------------------------
# CASOS ESPECIALES
# ----------------------------------------------------------

# ✓ Se pueden usar de diferentes tipos de datos
numero, texto, decimal = 42, "Hola", 3.14
print("\n--- Diferentes tipos de datos ---")
print(numero)    # Imprime: 42
print(texto)     # Imprime: Hola
print(decimal)   # Imprime: 3.14

# ✓ Intercambiar valores (sin necesidad de variable temporal)
x, y = 5, 10
print("\nAntes de intercambiar: x =", x, ", y =", y)  # x = 5 , y = 10
x, y = y, x      # ¡Ahora x=10 e y=5! (sin variable auxiliar)
print("Después de intercambiar: x =", x, ", y =", y)  # x = 10 , y = 5

# ❌ Error si FALTA un valor:
# a, b, c = 1, 2  
# Error: necesita 3 valores, pero solo hay 2

# ❌ Error si SOBRAN valores:
# a, b = 1, 2, 3  
# Error: demasiados valores (3) para solo 2 variables

