# Segue uma função queria uma nova lista com os strings
# que possuem caracteres alfanuméricos.
def alfanum_strings(strings):
    list = []
    for s in strings:
        if any(not c.isalnum() for c in s):
            pass
        else:
            list.append(s)
    return list


# Exemplo de aplicação 1:
list1 = ['fada123', 'fada', '3453', '123abc']
strings1 = alfanum_strings(list1)
print(strings1)

# Exemplo de aplicação 2:
list2 = ['^^7lka', '&&*kjks', '3453', 'abc/']
strings2 = alfanum_strings(list2)
print(strings2)
