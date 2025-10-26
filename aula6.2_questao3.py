import random
from collections import Counter

# Preenche as listas com 20 valores inteiros aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Cria uma lista de intersecção sem duplicatas
interseccao = sorted(list(set(lista1) & set(lista2)))

# Conta a quantidade de vezes que cada elemento aparece em cada lista
contagem1 = Counter(lista1)
contagem2 = Counter(lista2)

# Imprime as listas
print("Lista 1:", lista1)
print("Lista 2:", lista2)

# Imprime a lista de intersecção
print("Interseccao:", interseccao)

# Imprime a contagem de cada elemento
for elemento in interseccao:
    print(f"{elemento}: (lista1={contagem1[elemento]}, lista2={contagem2[elemento]})")