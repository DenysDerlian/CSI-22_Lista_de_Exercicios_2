# Segue a função que realiza a multiplicação entre
# duas matrizes representadas por listas
def matrix_multiply(a, b):
    dim = True
    for i in range(len(a)):
        if len(a[i]) != len(b):
            dim = False
            return "Dimensao incompativel"
    if dim:
        m = len(a)
        n = len(a[0])
        p = len(b[0])
        c = [[0 for _ in range(p)] for _ in range(m)]
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    c[i][j] += a[i][k] * b[k][j]
        return c


# Exemplo de aplicação 1:
A = [[1, 3, 4], [3, 8, 9]]
B = [[5, 9, 8], [5, 5, 5], [1, 2, 3]]
C = matrix_multiply(A, B)
print(C)

# Exemplo de aplicação 2:
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = matrix_multiply(A, B)
print(C)

# Teste de dimensão:
A = [[1, 3, 4], [3, 8]]
B = [[5, 9, 8], [5, 5, 5], [1, 2, 3]]
C = matrix_multiply(A, B)
print(C)
