# OPERACIONES CON NÚMEROS EN PYTHON
# En Python podemos hacer diferentes tipos de operaciones matemáticas

# ----------------------------------------------------------
# OPERADORES MATEMÁTICOS PRINCIPALES
# ----------------------------------------------------------
# +   suma
# -   resta
# *   multiplicación
# /   división normal (devuelve decimal/float)
# //  división entera (devuelve solo la parte entera)
# %   módulo (devuelve el residuo de la división)
# **  potencia (elevar a una potencia)

number = 10  # Guardamos el número 10 en una variable

# ----------------------------------------------------------
# DIVISIÓN NORMAL (/)
# ----------------------------------------------------------
# Devuelve un número con decimales (float)
# Ejemplo: 20 ÷ 4 = 5.0 (nota el .0, es un float, no int)

resultado1 = 20 / 4      # Dividimos 20 entre 4
print("División normal:")
print(resultado1)        # Imprime: 5.0
print(type(resultado1))  # Imprime: <class 'float'>

resultado2 = 15 / 4      # Dividimos 15 entre 4
print(resultado2)        # Imprime: 3.75


# ----------------------------------------------------------
# DIVISIÓN ENTERA (//)
# ----------------------------------------------------------
# Solo devuelve la parte entera, descarta los decimales
# Útil cuando solo necesitas el cociente sin residuo

# Ejemplo: 10 ÷ 10 = 1 (exacto)
result = number // 10
print("\nDivisión entera:")
print("El resultado es: ", result)  # Imprime: 1

# Ejemplo: 15 ÷ 4 = 3 (porque 15÷4 = 3.75, pero descartamos .75)
resultado3 = 15 // 4
print(resultado3)        # Imprime: 3

# Ejemplo: 20 ÷ 3 = 6 (porque 20÷3 = 6.666..., pero descartamos los decimales)
resultado4 = 20 // 3
print(resultado4)        # Imprime: 6


# ----------------------------------------------------------
# MÓDULO (%)
# ----------------------------------------------------------
# Devuelve lo que sobra (el residuo) después de dividir
# Útil para saber si un número es par o impar, etc.

# Ejemplo: 15 ÷ 4 = 3 con residuo 3
residuo = 15 % 4
print("\nMódulo (residuo):")
print(residuo)           # Imprime: 3

# ¿Es 10 divisible entre 2?
residuo2 = 10 % 2        # 10 ÷ 2 = 5 exacto, residuo 0
print(residuo2)          # Imprime: 0 (es divisible)

# ¿Es 7 divisible entre 2?
residuo3 = 7 % 2         # 7 ÷ 2 = 3 con residuo 1
print(residuo3)          # Imprime: 1 (no es divisible)


# ----------------------------------------------------------
# POTENCIA (**)
# ----------------------------------------------------------
# Eleva un número a una potencia
# Ejemplo: 5 ** 2 significa 5 al cuadrado = 5 × 5 = 25

cuadrado = 5 ** 2        # 5 al cuadrado
print("\nPotencia:")
print(cuadrado)          # Imprime: 25

cubo = 3 ** 3            # 3 al cubo = 3 × 3 × 3 = 27
print(cubo)              # Imprime: 27

potencia = 2 ** 8        # 2 a la octava = 256
print(potencia)          # Imprime: 256