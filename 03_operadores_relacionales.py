# OPERADORES RELACIONALES (DE COMPARACIÓN)
# Se usan para COMPARAR dos valores y obtener un resultado: True o False
# Esto es fundamental para tomar decisiones en el código

# ----------------------------------------------------------
# OPERADORES RELACIONALES
# ----------------------------------------------------------
# >   mayor que
# <   menor que
# >=  mayor o igual que
# <=  menor o igual que
# ==  igual a (¡OJO! es doble igual, no confundir con = que es asignación)
# !=  diferente a (no igual)

number_one = 10   # Guardamos el número 10
number_two = 20   # Guardamos el número 20

# ----------------------------------------------------------
# COMPARACIÓN: ¿Son iguales?
# ----------------------------------------------------------
# ¿Es 10 igual a 20?

result = number_one == number_two  # Comparamos: ¿10 == 20?
print("¿Es 10 igual a 20?")
print("El resultado es: ", result)  # Imprime: False
print(type(result))  # Imprime: <class 'bool'>
# ↑ El resultado SIEMPRE es un booleano (True o False)

# ----------------------------------------------------------
# OTROS EJEMPLOS DE COMPARACIONES
# ----------------------------------------------------------

print("\n--- MÁS EJEMPLOS ---")

# ¿Es 10 mayor que 5?
print("¿10 > 5?", 10 > 5)        # Imprime: True

# ¿Es 10 menor que 5?
print("¿10 < 5?", 10 < 5)        # Imprime: False

# ¿Es 10 mayor o igual a 10?
print("¿10 >= 10?", 10 >= 10)    # Imprime: True

# ¿Es 10 menor o igual a 5?
print("¿10 <= 5?", 10 <= 5)      # Imprime: False

# ¿Es 10 diferente a 5?
print("¿10 != 5?", 10 != 5)      # Imprime: True

# ¿Es 10 diferente a 10?
print("¿10 != 10?", 10 != 10)    # Imprime: False

# ----------------------------------------------------------
# COMPARACIONES CON STRINGS (Texto)
# ----------------------------------------------------------
# También se pueden comparar strings

nombre1 = "Juan"
nombre2 = "Maria"

print("\n--- COMPARACIONES CON STRINGS ---")
print("¿Juan == Maria?", nombre1 == nombre2)  # False
print("¿Juan != Maria?", nombre1 != nombre2)  # True

# ----------------------------------------------------------
# IMPORTANTE: = vs ==
# ----------------------------------------------------------
# = es ASIGNACIÓN (guardar un valor)
# == es COMPARACIÓN (pregunta si dos valores son iguales)

# ✓ Correcto:
x = 5              # Asignamos 5 a x (con =)
resultado = (x == 5)  # Comparamos si x es igual a 5 (con ==)
print("\n--- DIFERENCIA = vs == ---")
print("x = 5 (asignación)")
print("¿x == 5? (comparación)", resultado)  # True

# ✗ Incorrecto (esto causaría error):
# if x = 5:  # ❌ Error: no se puede usar = en comparación
#    print("x es 5")