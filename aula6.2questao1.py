import random

# Gera aleatoriamente 20 valores inteiros entre -100 e 100
valores = [random.randint(-100, 100) for _ in range(20)]

# Imprime a lista ordenada sem modificar a lista original
print("Lista ordenada:", sorted(valores))

# Imprime a lista original
print("Lista original:", valores)

# Encontra o índice do maior valor da lista
indice_maior = valores.index(max(valores))
print("Índice do maior valor:", indice_maior)

# Encontra o índice do menor valor da lista
indice_menor = valores.index(min(valores))
print("Índice do menor valor:", indice_menor)