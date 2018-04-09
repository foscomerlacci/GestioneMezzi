# def digit_sum(n):
#     somma = 0
#     lista = list(str(n))
#
#     for x in range(len(lista)):
#         somma += int(lista[x])
#         print(somma)
#     print (somma)
#
# digit_sum(1025)


# def is_prime(x):
#     if x >= 3:
#         for n in range(2,(x-1)):
#             if x % n == 0:
#                 return False
#             else:
#                 return True
#     else:
#         return False
#
# if is_prime(5) == True:
#     print("sei un numero primo")


# def reverse(text):
#     lettere = list(str(text))
#     erettel = []
#     risultato = "a"
#     print(lettere)
#     print(len(lettere)-1)
#     counter = len(lettere)-1
#     for lettera in lettere:
#         erettel.append(lettere[counter])
#         counter -= 1
#     print ("".join(erettel))
#
#
#
#
# reverse("Python!")


# score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
#          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
#          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
#          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
#          "x": 8, "z": 10}
#
# def scrabble_score(word):
#     parole = list(word.lower())
#     risultato = 0
#     for parola in parole:
#         risultato += score[parola]
#     print(risultato)
#
# scrabble_score("Ciao")


# def censor(text,word):
#     parole = text.split()
#     for x in range(0,len(parole)):
#         if parole[x] == word:
#             parole[x] = "*"*len(parole[x])
#     print(" ".join(parole))
#
# censor("questa è la frase la la","la")


# def count(sequence,item):
#     counter = 0
#     for x in range(0,len(sequence)):
#         if sequence[x] == item:
#             counter += 1
#     print(counter)
#
# count([3,6,9,1,3,6,3],3)

# def purify(lista):
#     even = []
#     for item in lista:
#         if item % 2 == 0:
#             even.append(item)
#     print(even)
#
# purify([1,2,3,4,5,6,7,])


# def median(lista):
#     lista.sort()
#     print(lista)
#     print(len(lista))
#     if len(lista) == 1:
#         ris = lista[0]
#         print(ris)
#     elif len(lista) % 2 == 0:
#         ris = (lista[int(len(lista)/2)] + lista[int((len(lista)/2)-1)])/2
#         print(ris)
#     else:
#         ris = lista[int((len(lista)-1)/2)]
#         print(ris)
# median([4,5,5,14,21,4,1,9,2,3,7])


# scores = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
#
# def grades_sum(scores):
#     total = 0
#     for grade in scores:
#         total += grade
#         print(total)
#     return total
#     print(total)
#
# grades_sum(scores)

# my_dict = {
#     "nome": "Lillo",
#     "cognome": "Alfonsi",
#     "anni": 34,
#     }
#
# print(my_dict.items())

# to_21 = range(1,22)
# odds = to_21[::2]
# middle_third = to_21[7:14:1]
# print(odds, middle_third)

# threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
# print(threes_and_fives)

# garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
# message = garbled[::-2]
# print(message)


# def is_prime(x):
#     for n in range(2,x):
#         if x % n == 0:
#             print(0)
#             return False
#     else:
#         if x < 2:
#             print(0)
#             return False
#         else:
#             print(1)
#             return True
#
# is_prime(5)

# class Car(object):
#     condition = "new"
#     def __init__(self, model, color, mpg):
#         self.model = model
#         self.color = color
#         self.mpg   = mpg
#
#     def display_car(self):
#         print("This is a {} {} with {} MPG.".format(self.color, self.model, self.mpg))
#
#     def drive_car(self):
#         self.condition = "used"
#
#
# #my_car = Car("DeLorean", "silver", 88)
# #print my_car.condition
# #my_car.drive_car()
# #print my_car.condition
#
# class ElectricCar(Car):
#     def __init__(self, model, color, mpg, battery_type):
#         self.model = model
#         self.color = color
#         self.mpg   = mpg
#         self.battery_type = battery_type
#
#     def drive_car(self):
#         self.condition = "like new"
#
#
# my_car = ElectricCar("macchinina", "rossa", 12,"molten salt")
# print(my_car.condition)
# my_car.drive_car()
# print (my_car.condition)

# class Point3D(object):
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __repr__(self):
#         return "({}, {}, {})".format (self.x, self.y, self.z)
#
# my_point = Point3D(4,5,6)
#
# print(my_point)

# my_file = open("/home/utente/GestioneMezzi/GestioneMezzi/templates/base.html","r")
# print(my_file.readline())
# print(my_file.readline())



# lista = []
#
# with open("/home/utente/GestioneMezzi/GestioneMezzi/templates/base.html") as my_file:
#     for line in my_file:
#         lista.append(line)
# my_file.close()
#
#
# for count, valore in enumerate(lista):
#     print(count, valore)
#
# for x in lista:
#     print(x)
#
# print(lista)

# import feedparser
#
# feeds = feedparser.parse("http://xml.corriereobjects.it/rss/homepage.xml")
#
# for feed in feeds.entries:
#     # print(feed.title, feed.link,str.upper(feed.author))
#     print(feed.title, feed.link)
#
# print("Ci sono {} post".format(len(feeds)))

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = None
# numbers.append([n + 1 for n in range(3)])
for x in range(3):
    numbers.append(x + 1)

strings.append("hello")
strings.append("world")



# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)




