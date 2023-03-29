# Segue uma função, usando generator, que
# percorre uma lista do final para frente
def reversed_list(lista):
    for i in reversed(lista):
        yield i


# Exemplo de aplicação:
lista = [4, 7, 8]
iterador = reversed_list(lista)

print(next(iterador))
print(next(iterador))
print(next(iterador))
