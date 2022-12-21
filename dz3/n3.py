import math


def main():
    """Квадратное уравнение.

    Вводятся коэффициенты уравнения.

    Выводятся корни уравнения.
    """
    a= int(input("Введите a: "))
    b= int(input("Введите b: "))
    c= int(input("Введите c: "))
    d = math.pow(b, 2) - 4*a*c
    if d > 0:
        print("x\u2081 = {:1.2f}".format((-b-math.sqrt(d)) / (2*a)))
        print("x\u2082 = {:1.2f}".format((-b+math.sqrt(d)) / (2*a)))
    elif d == 0:
        print("x\u2081,\u2082 = {:1.2f}".format((-b-math.sqrt(d)) / (2*a)))
    else:
        print("x\u2081,\u2082 = {:1.2f} \u00b1 {:1.2f}i".format(-b / (2*a), math.sqrt(abs(d)) / (2*a)))


if __name__ == "__main__":
    main()