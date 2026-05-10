# zip

# La función zip() se utiliza para combinar elementos de varias secuencias (como listas, tuplas, etc.) en una sola secuencia de tuplas. Cada tupla contiene un elemento de cada una de las secuencias originales en la misma posición.

users = ["user1", "user2", "user3"]
courses = ("Python", "Django", "Ruby on Rails")
scores = [10, 9, 8]

# paired = list(zip(users, courses, scores))
# print(paired)  # Imprime: [('user1', 'Python'), ('user2', 'Django'), ('user3', 'Ruby on Rails')]


paired = tuple(zip(users, courses, scores))
print(paired)  # Imprime: (('user1', 'Python', 10), ('user2', 'Django', 9), ('user3', 'Ruby on Rails', 8))