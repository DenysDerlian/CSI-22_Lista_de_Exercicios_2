# Segue uma função que filtra os números pares de uma
# lista de números aleatórios utilizando
# a função de filtragem e a função lambda

# Lista exemplo:
num = [3, 7, 2, 9, 4, 8, 5, 6, 1, 0]

even = list(filter(lambda x: x % 2 == 0, num))

print(even)
