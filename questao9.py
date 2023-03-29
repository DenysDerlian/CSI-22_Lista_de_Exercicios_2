# Segue uma função que aplica uma função para cada linha
# de uma matriz e retorna o resultado das operações
# em cada linha em uma lista
def line_operation(function, matrix):
    return list(map(function, matrix))


# Exemplo de aplicação:
# Suponha que o resultado segue na seguinte matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

# Caso se queira utilizar a função somatória para cada linha
result = line_operation(sum, matriz)
print(result)
