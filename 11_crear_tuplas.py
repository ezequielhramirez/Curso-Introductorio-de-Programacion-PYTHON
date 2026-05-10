
# Las tuplas son similares a las listas, pero son INMUTABLES (no se pueden modificar después de crear).
# Se definen con paréntesis () en lugar de corchetes [].

# Crear tuplas
#                0         1     2
#                -3         -2     -1
settings = ("localhost", 8080, True)


print ("Tupla settings:", settings)
print (type(settings))  # <class 'tuple'>

print("--------------------------------------------")

# settings[0] = "localhost"  # ERROR: no se pueden modificar las tuplas


print (settings[0])  # localhost
print (settings[1])  # 8080
print (settings[2])  # True


print("--------------------------------------------")



# En python podemos crear crear tuplas con o sin paréntesis, pero para una tupla con un solo elemento se necesita la coma al final.

#                0         1     2
#                -3         -2     -1
settings = ("localhost", 8080, True)

numbers = 1, # Tupla con un solo elemento (se necesita la coma)

# numbers = 1, 2, 3, 4, 5  # También se pueden crear sin paréntesis

# print (numbers)  # (1, 2, 3, 4, 5)
print (numbers)  # (1,)

print (type(numbers))  # <class 'tuple'>