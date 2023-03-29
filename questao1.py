# Segue função que remove todas as tuplas vazias de uma lista de tuplas.
def remove_empty_tuples(lista):
    new_list = []
    for tupla in lista:
        if len(tupla) > 0:
            new_list.append(tupla)
    return new_list


# Exemplo de utilização:
tuplas_lista = [(), (1, 2, 3), (), (9,), (), (), (4, 5, 6, 7, 8), (), ()]
tuplas_nova_lista = remove_empty_tuples(tuplas_lista)
print(tuplas_nova_lista)
