def manipula_lista():
    # Solicita números inteiros ao usuário
    numeros = []
    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para parar): ")
        if entrada.lower() == 'fim':
            break
        try:
            numeros.append(int(entrada))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    # Verifica se a lista tem pelo menos 4 valores
    if len(numeros) < 4:
        print("A lista deve ter pelo menos 4 valores.")
        return

    # Imprime a lista original
    print("Lista original:", numeros)

    # Imprime os 3 primeiros elementos
    print("3 primeiros elementos:", numeros[:3])

    # Imprime os 2 últimos elementos
    print("2 últimos elementos:", numeros[-2:])

    # Imprime a lista invertida
    print("Lista invertida:", numeros[::-1])

    # Imprime os elementos de índice par
    print("Elementos de índice par:", numeros[::2])

    # Imprime os elementos de índice ímpar
    print("Elementos de índice ímpar:", numeros[1::2])

manipula_lista()