import math
def n1():
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    print("{}+{}={:1.2f}".format(x,y,x+y))
    print("{}-{}={:1.2f}".format(x,y,x-y))
    print("{}*{}={:1.2f}".format(x,y,x*y))
    print("{}/{}={:1.2f}".format(x,y,x/y))
    print("{} в степени {}={:1.2f}".format(x,y,x**y))
    print("Остаток от деления {} на {}={:1.2f}".format(x,y,x%y))
    print("Целая часть от деления {} на {}={:1.2f}".format(x,y,x//y))

def n2():
    name = input("Введите своё имя: ")
    print("Добрый день, {}".format(name))

def n3 ():
    string = input("Введите строку: ")
    print(string[-2:][::-1])

def n4 ():
    r = float(input("Введите радиус круга:"))
    print("Площадь круга ={:1.2f}".format(r**2*math.pi))

def main():
    x = input("Введите номер задания (1-4). 5 - завершение: ")
    if x == "1":
        n1()
        main()
    elif x == "2":
        n2()
        main()
    elif x == "3":
        n3()
        main()
    elif x == "4":
        n4()
        main()
    elif x == "5":
        pass
    else:
        print("Введён неверный номер")

main()
