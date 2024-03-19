# Criando uma lista de números
numeros = [1, 2, 3, 4, 5]

# Acessando elementos da lista
print(numeros[0])  # Output: 1
print(numeros[2])  # Output: 3

# Alterando elementos da lista
numeros[1] = 10
print(numeros)  # Output: [1, 10, 3, 4, 5]

# Adicionando elementos à lista
numeros.append(6)
print(numeros)  # Output: [1, 10, 3, 4, 5, 6]

# Removendo elementos da lista
numeros.remove(3)
print(numeros)  # Output: [1, 10, 4, 5, 6]

# Tamanho da lista
tamanho = len(numeros)
print(tamanho)  # Output: 5

# Verificando a existência de um elemento na lista
existe = 4 in numeros
print(existe)  # Output: True

# Iterando sobre os elementos da lista
for numero in numeros:
    print(numero)

#-------------------------------------------------------
# Tuplas
#-------------------------------------------------------

# Criando uma tupla de nomes
nomes = ("Alice", "Bob", "Charlie")

# Acessando elementos da tupla
print(nomes[0])  # Output: Alice
print(nomes[2])  # Output: Charlie

# Iterando sobre os elementos da tupla
for nome in nomes:
    print(nome)