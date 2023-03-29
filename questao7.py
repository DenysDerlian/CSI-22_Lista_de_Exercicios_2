# Segue uma função que, usando generator,
# cria uma lista infinita com todos os números primos
def prime_generator():
    num = {}
    n = 2
    while True:
        if n not in num:
            yield n
            num[n * n] = [n]
        else:
            for p in num[n]:
                num.setdefault(p + n, []).append(p)
            del num[n]
        n += 1


# Exemplo de aplicação
prime = prime_generator()

for i in range(10):
    print(next(prime))
