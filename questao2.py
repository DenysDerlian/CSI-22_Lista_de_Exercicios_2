# Segue uma função que calcula a média de cada tupla interna e
# retorna uma nova tupla com as médias.
def media_tuplas(tuplas):
    n_tuplas = int(len(tuplas))
    medias = []
    for i in range(n_tuplas):
        soma = 0
        n_valores = 0
        for j in range(len(tuplas[i])):
            soma += tuplas[i][j]
            n_valores += 1
        medias.append(soma / n_valores)
    return tuple(medias)


# Exemplo de utilização 1
tuplas1 = ((1, 2), (4, 5, 6), (7, 8, 9, 10))
medias1 = media_tuplas(tuplas1)
print(medias1)

# Exemplo de utilização 2
tuplas2 = ((2, 3, 4), (3, 4, 5, 6), (2, 4), (4, 8, 9))
medias2 = media_tuplas(tuplas2)
print(medias2)
