# zadanie 1

def porownaj(a_list, b_list):
    ab_list = []

    for x in range(len(a_list)):
        if x % 2 == 0:
            ab_list.append(a_list[x])

    for x in range(len(b_list)):
        if x % 2 == 1:
            ab_list.append(b_list[x])

    return ab_list

ab_list = porownaj(['a','b','c','d','e'],[1,2,3,4,5])

print(ab_list)

# zadanie 2

def getInfo(data_text):

    dict = {
        "length": len(data_text),
        "letters": list(data_text),
        "big_letters": data_text.upper(),
        "small_letters": data_text.lower()
    }
    return dict

print(getInfo("Student"))

# zadanie 3
def cut(text, letter):
    result = text.replace(letter, '')
    return result

print(cut("anakonda", "a"))

# zadanie 4
def convertTemp(value, temperature_type):

    if temperature_type.lower() == "kelvin":
        result = value + 273

    elif temperature_type.lower() == "fahrenheit":
        result = value * 2 + 30

    elif  temperature_type.lower() == "rankine":
        result = (value + 273.15) * 9/5
    else:
        result = "bad temperature type"

    return result

print(convertTemp(20,"kelvin"))
print(convertTemp(20,"fahrenheit"))
print(convertTemp(20,"rankine"))
print(convertTemp(20,"wrongType"))

# zadanie 5

class Calculator:
    def add(self,a, b):
        return a+b
    def difference(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b != 0:
            return a/b
        else:
            return "nie wolno dzielic przez 0"


cal = Calculator()
print(cal.add(2,2))
print(cal.difference(2,2))
print(cal.multiply(2,2))
print(cal.divide(2,2))

# zadanie 6
class ScienceCalculator(Calculator):
    def pow(self,a,b):
        result = 1
        for x in range(b):
            result *= a
        return result

cal2 = ScienceCalculator()

print(cal2.pow(5,3))

# zadanie 7
def reverse(string):
    return string[::-1]

print(reverse("pieseł"))

# zadanie 9
import file_manager

f = file_manager.Filemanager('tekst.txt')
f.readfile()
f.updatefile('dodany tekst :)')
f.readfile()