import random

# Gera lista com 20 elementos aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]
print("Lista original:", lista)

# Encontra o intervalo com maior quantidade de números negativos
max_negativos = 0
inicio_intervalo = 0
fim_intervalo = 0
negativos_atual = 0
inicio_atual = 0

for i, num in enumerate(lista):
    if num < 0:
        negativos_atual += 1
        if negativos_atual > max_negativos:
            max_negativos = negativos_atual
            inicio_intervalo = inicio_atual
            fim_intervalo = i
    else:
        negativos_atual = 0
        inicio_atual = i + 1

# Deleta o intervalo com maior quantidade de números negativos
if max_negativos > 0:
    del lista[inicio_intervalo:fim_intervalo+1]
    print("Lista editada:", lista)
else:
    print("Não há números negativos na lista.")
    