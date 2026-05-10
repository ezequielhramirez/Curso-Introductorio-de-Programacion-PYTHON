#Tuplas


#Las tuplas son inmutables, es decir, no se pueden modificar después de su creación. Se definen utilizando paréntesis ().
#Sintaxis: tupla = (elemento1, elemento2, elemento3, ...)

#Ejemplo de tupla
print("\n--- EJEMPLO DE TUPLA ---")
mi_tupla = (1, 2, 3, "Hola", [4, 5], (6, 7))

print("Tupla:", mi_tupla)
print("Tipo de dato:", type(mi_tupla)) 
print("Número de elementos en la tupla:", len(mi_tupla))


#           0               1       2   
#           -1             -2      -3   
settings = ("localhost", 8080, True)

print("\n--- EJEMPLO DE TUPLA DE CONFIGURACIÓN ---")
print("Tupla de configuración:", settings)
print("Host:", settings[0])  # Accediendo al host
print("Puerto:", settings[1])  # Accediendo al puerto
print("¿Es seguro?", settings[2])  # Accediendo a la configuración de seguridad
print(settings[-1])  # Accediendo al último elemento (True)

# Las tuplas también pueden contener otros tipos de datos, como listas o incluso otras tuplas.

