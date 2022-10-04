# import sys
# # zad 1
# #a
# lista = []
# for x in range(1, 11, 1):
#     lista.append(x)
# print(lista)
# #b
# lista = []
# for x in range(0, 11, 1):
#     lista.append(x*2)
# print(lista)
# #c
# lista = []
# for x in range(1, 11, 1):
#     lista.append(x**2)
# print(lista)
# #d
# lista = []
# for x in range(1, 11, 1):
#     lista.append(0)
# print(lista)
# #e
# lista = []
# for x in range(1, 11, 1):
#     if (x%2 == 0):
#         lista.append(1)
#     else:
#         lista.append(0)
# print(lista)
# #f
# lista = []
# for x in range(0, 10, 1):
#     if (x < 5):
#         lista.append(x)
#     else:
#         lista.append(x-5)
#
# print(lista)
# #zad 2
# #a
# print('zadanie 2')
# lista = []
# x = 0
# while x < 11:
#     lista.append(x)
#     x += 1
# print(lista)
# #b
# lista = []
# x = 0
# while x < 11:
#     lista.append(x*2)
#     x += 1
# print(lista)
# #c
# lista = []
# x = 0
# while x < 11:
#     lista.append(x**2)
#     x += 1
# print(lista)
# #d
# lista = []
# x = 0
# while x < 11:
#     lista.append(0)
#     x += 1
# print(lista)
# #e
# lista = []
# x = 0
# while x < 11:
#     if (x%2 == 0):
#         lista.append(1)
#     else:
#         lista.append(0)
#     x += 1
# print(lista)
# #f
# lista = []
# x = 0
# while x < 10:
#     if (x < 5):
#         lista.append(x)
#     else:
#         lista.append(x-5)
#     x += 1
# print(lista)
# #zad 3
lista1 = [1, 4, 16, 9, 9, 7, 4, 9, 11]
# def ile_ujemnych(zad3):
#     ile=0
#     for x in zad3:
#         if(x<0):
#             ile +=1
#         else:
#             continue
#     print(ile)
# ile_ujemnych(lista1)
# #zad 4
# def iloczyn(zad4):
#     wynik=1
#     for x in zad4:
#         wynik *= x
#     print(wynik)
# iloczyn(lista1)
# #zad 5
# def minmax(zad5):
#     min = sys.maxsize
#     max = -sys.maxsize - 1
#     for x in zad5:
#         if(x<min):
#             min=x
#         if(x>max):
#             max=x
#     print((min,max))
# minmax(lista1)
#zad 6
# def przemiennosc(zad6):
#     x=0
#     wynik = 0
#     while x<len(lista1)
#         if(x%2==1):
#             wynik -=lista1[x]
#         else:
#             wynik +=lista1[x]
#         x+=1
#     print(wynik)
# przemiennosc(lista1)
#zad 7
# print('Podaj liczbe by dodac ja do listy')
# a = int(input())
# blad = 0
# if len(lista1)>10:
#     print('lista posiada juz 10 liczb')
# else:
#     for x in lista1:
#         if(x==a):
#             blad=1
# if blad==0:
#     lista1.append(a)
# else:
#     print('jest juz taka liczba w liscie')
# print(lista1)
#zad8
lista2 = []
for x in range(2,10001,1):
    lista2.append(x)
for p in lista2:
    for a in range(2,10001,1):
        if(x%a==0 & x!=a):
            lista2.remove(p)
print(lista2)
