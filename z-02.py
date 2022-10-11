# zad1


def mult(a):
    suma = 1
    for n in a:
        suma *= n
    return suma
print(mult([3, 5, 7]))
print(mult(range(2, 8, 2)))


# zad 2
def mult_ints(a):
    suma = 1
    for n in a:
        if type(n) != int:
            continue
        suma *= n
    return suma
print(mult_ints([3, 3.14, 5, "abc", 7]))


# zad3
def multiply(*args):
    suma = 1
    for n in args:
        suma *= n
    return suma


print(multiply(3, 5, 7))

# zad 4


def multiply_ints(*args):
    suma = 1
    for i in args:
        if type(i) != int:
            continue
        suma *= i
    return suma


print(multiply_ints(3, 3.14, 5, "abc", 7))

# zad 5


def make_car(firma, model, **kwargs):
    slownik = kwargs
    slownik['firma'] = firma
    slownik['model'] = model
    return slownik

print(make_car("kia", "picante"))
