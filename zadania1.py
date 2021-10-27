import json


# Zadanie 1
str = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
print(str)

# Zadanie 2
imie = "Konrad"
nazwisko = "Wirchanowicz"
litera_1 = imie[2]
litera_2 = nazwisko[3]

sum1 = 0
sum2 = 0

for el in str:
    if el == litera_1:
        sum1 += 1

    if el == litera_2:
        sum2 += 1


str1 = "W tekscie jest %i liter %s oraz %i liter %s"

print(sum1)
print(sum2)
print(litera_1)
print(litera_2)

print(str1 % (sum1, litera_1, sum2, litera_2))

# zadanie 4

str2 = "Jakis String"
print(dir(str2))
help(str2.lower)

# zadanie 5
name = "Konrad"
surname = "Wirchanowicz"

name = name[::-1]
surname = surname[::-1]

name = name.capitalize()
surname = surname.capitalize()
print(name + " " + surname)

# zadanie 6

list = []
for i in range(10):
    list.append(i + 1)

print(list)
temp = list

list = list[slice(5)]
sliced_list = temp[slice(5, 10)]
print(list)
print(sliced_list)

# zadanie 7

list = list + sliced_list
list.insert(0, 0)
list.sort(reverse=True)
print(list)

# zadanie 8
lista_studentow = [
    (155551, "Konrad Jakis"),
    (155552, "Adam Jakis"),
    (155553, "Mikołaj Jakis"),
    (155554, "Maciek Jakis"),
    (155555, "Roman Jakis"),
    (155556, "Kinga Jakis"),
    (155557, "Wiesław Jakis")
    ]
print(lista_studentow)

# zadanie 9
dct = dict((x, y) for x, y in lista_studentow)


for x in dct:
    dct[x] = {
        "imie": dct[x],
        "wiek": 20,
        "mail": "mail@test",
        "rok urodzenia": 2000,
        "adres": "adres 1/12"
    }

print(dct)

# zadanie 10
tel_numbers = [999, 998, 997, 997]
tel_numbers = set(tel_numbers)
print(tel_numbers)

#zadanie 11

for x in range(10):
    print(x + 1, end=" ")

#zadanie 12
print()
for x in range(100, 15, -5):
    print(x, end=" ")

print()
#zadanie 13

lista_slownikow = []

dict1 = {
    "orange": "pomaranczowy",
    "black": "czarny",
    "green": "zielony"
}

dict2 = {
    "student": "ocena mierna",
    "magister": "ocena dobra",
    "profesor": "god level"
}

dict3 = {
    "audi": "Niemcy",
    "polonez": "Polska",
    "jeep": "USA"
}

lista_slownikow.append(dict1)
lista_slownikow.append(dict2)
lista_slownikow.append(dict3)

print('kolory: \n' + json.dumps(lista_slownikow[0]) + '\noceny: \n' + json.dumps(lista_slownikow[1]) + '\nauta: \n' + json.dumps(lista_slownikow[2]))