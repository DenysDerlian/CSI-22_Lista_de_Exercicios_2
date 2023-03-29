# Segue uma função que verifica se todos os caracteres de
# uma string estão presentes em uma outra string.
def char_verify(string1, string2):
    for char in string1:
        if char not in string2:
            return False
    return True


# Exemplo de aplicação 1:
string1 = "AbcD1"
string2 = "EFGAbcD12"
print(char_verify(string1, string2))

# Exemplo de aplicação 2:
string3 = "AbcD1"
string4 = "EFGAbdD12"
print(char_verify(string3, string4))
