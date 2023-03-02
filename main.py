from functools import reduce
paises = input("Digite los paises que quieras: ")
listapaises = paises.split(",")
print(set(sorted(listapaises)))


lista = [1,2,3,4,5,6,7,8,9,10]

def impar(x):
    if x % 2 == 0:
        return False

    return True

def suma(x, z):
    return x + z

total = list(filter(impar, lista))
print(total)
print(int(reduce(suma, total)))


