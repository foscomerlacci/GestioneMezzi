__author__ = 'utente'


t = ("uno", "due", "tre", "quattro")
int = t[0:2]
print(int)
print(type(int))

l = ["cinque", "sei", "sette", "otto", "nove", "dieci", ]

for x in l:
    print(x, end=" ")
print("\n")

lista = ["primo", "secondo", "terzo"]
atsil = list(reversed(lista))
atsil.reverse()

# print(dir(lista))



print(lista[::-1])
print(atsil)
print(t[::-1])
print(list(reversed(t)))
newt = list(t)
print(type(newt))

