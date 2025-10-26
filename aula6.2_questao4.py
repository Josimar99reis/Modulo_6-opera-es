def intercala_listas(lista1, lista2):
    # Encontra o tamanho mínimo entre as duas listas
    tamanho_minimo = min(len(lista1), len(lista2))

    # Intercala os elementos das listas até o tamanho mínimo
    lista_intercalada = [item for par in zip(lista1[:tamanho_minimo], lista2[:tamanho_minimo]) for item in par]

    # Adiciona os elementos remanescentes da lista maior
    lista_intercalada += lista1[tamanho_minimo:] + lista2[tamanho_minimo:]

    return lista_intercalada

def main():
    # Lê a quantidade de elementos da lista 1
    qtd_elementos_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))

    # Lê os elementos da lista 1
    lista1 = list(map(int, input(f"Digite os {qtd_elementos_lista1} elementos da lista 1: ").split()))

    # Lê a quantidade de elementos da lista 2
    qtd_elementos_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))

    # Lê os elementos da lista 2
    lista2 = list(map(int, input(f"Digite os {qtd_elementos_lista2} elementos da lista 2: ").split()))

    # Intercala as listas
    lista_intercalada = intercala_listas(lista1, lista2)

    # Imprime a lista intercalada
    print("Lista intercalada:", lista_intercalada)

if __name__ == "__main__":
    main()