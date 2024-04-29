import argparse

def ordenar_lista(lista, ascendente=True):
    return sorted(lista, reverse=not ascendente)

if __name__ == "__main__":
    # Configurar el análisis de argumentos de la línea de comandos
    parser = argparse.ArgumentParser(description='Ordenar una lista en orden ascendente o descendente.')
    parser.add_argument('lista', metavar='N', type=int, nargs='+',
                        help='la lista de números a ordenar')
    parser.add_argument('--descendente', action='store_true',
                        help='ordenar en orden descendente')

    # Analizar los argumentos de la línea de comandos
    args = parser.parse_args()

    # Ordenar la lista
    lista_ordenada = ordenar_lista(args.lista, ascendente=not args.descendente)

    # Imprimir la lista ordenada
    print("Lista ordenada:", lista_ordenada)
