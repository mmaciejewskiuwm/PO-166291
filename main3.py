import math
#zad 1
# class Point(object):
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     @staticmethod
#     def distance(point1, point2):
#         dx = point1.x - point2.x
#         dy = point1.y - point2.y
#         return math.sqrt(dx**2 + dy**2)
#
# Point1 = Point(16,12)
# Point2 = Point(12,13)
# print(Point.distance(Point1,Point2))
#zad 2
# class Adres:
#     def __init__(self, nr, ulica,mst,kp, nrm = None):
#         self.nr=nr
#         self.ulica=ulica
#         self.mst = mst
#         self.kp = kp
#         if (nrm is not None):
#             self.nrm=nrm
#         else:
#             self.nrm=None
#     def show(self):
#         if(self.nrm):
#             print('Adres to',self.ulica,self.nr,'/',self.nrm)
#             print('Miasto :',self.mst,',Kod pocztowy : ',self.kp )
#         else:
#             print('Adres to', self.ulica, self.nr)
#             print('Miasto :', self.mst, ',Kod pocztowy : ', self.kp)
#     def comes_before(self, other):
#         skp = self.kp
#         okp = other.kp
#         for x in range(len(skp)):
#             l1 = skp[x]
#             l2 = okp[x]
#             if(l2>l1):
#                 wieksza = 0
#                 break
#             elif(l1>l2):
#                 wieksza = 1
#                 break
#             else:
#                 continue
#         if(wieksza==0):
#             return print('wiekszy kod pocztowy to',okp)
#         elif(wieksza==1):
#             return print('wiekszy kod pocztowy to',skp)
#         else:
#             print("sa takie same kody pocztowe")
#             return None
#
#
#
# adres1=Adres(13,'Miastowa','Bydgoszcz','21-37')
# adres2=Adres(21,'Wiesna','Bialysok','22-15')
# Adres.show(adres1)
# Adres.show(adres2)
# Adres.comes_before(adres1,adres2)
#zad 3
# class SodaCan:
#     def __init__(self,h,r):
#         self.h = h
#         self.r = r
#     def get_volume(self):
#         r = self.r
#         h = self.h
#         return ((math.pi)*(r**2)*h)
#     def get_surface_area(self):
#         r = self.r
#         h = self.h
#         return (2*(math.pi)*r*(r+h))
# soda1=SodaCan(21,37)
# print(SodaCan.get_surface_area(soda1))
# print(SodaCan.get_volume(soda1))
#zad 4
# class Car:
#     def __init__(self,wp,maks,pp = None):
#         self.wp=wp
#         self.maks = maks
#         self.pp= 0
#     def drive(self, odl: float) -> None:
#         spalanie = odl / self.wp
#         if spalanie > self.pp:
#             print('Samochjod zgasl.')
#             return None
#         self.pp -= odl / self.wp
#
#     def get_fuel_level(self) -> float:
#         return self.pp
#
#     def add_fuel(self, ile: float) -> None:
#         if ile + self.pp > self.maks:
#             print('Masz za malego baka')
#             return None
#         self.pp += ile
# my_car = Car(20, 40)
# my_car.add_fuel(40)
# my_car.drive(100)
# print(my_car.get_fuel_level())
#zad 5
class Student:
    def __init__(self, imie, nazwisko, *args):
        self.imie = imie
        self.nazwisko = nazwisko
        self.quizy = len(args)
        try:
            suma = 0
            for i in args:
                suma += i
            self.quizyavr = suma / self.liczba_quizuw
        except ZeroDivisionError:
            self.quizyavr = 0


    def add_quiz(self, wynik):
        self.quizyavr = ((self.quizyavr * self.quizy) + wynik) / (self.quizy + 1)
        self.quizy += 1

    def get_total_score(self):
        return self.quizy * self.quizyavr

    def get_average_score(self):
        return self.srednia_quizuw

