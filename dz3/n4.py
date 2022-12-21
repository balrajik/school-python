import math
import cmath


def choose(name):
    """ Ввод коэффициента с выбором типа.

    Параметры:
        name - имя коэффициента

    Возвращает:
        x - значение коэффициента
    """
    type = input("1 - Комплексное число, 2 - Обычное число : ")
    if type == '1':
        x = complex(input("{} = ".format(name)))
        return x
    elif type == '2':
        x = int(input("{} = ".format(name)))
        return x


def main():
    """Квадратное уравнение.

    Происхолит вызов функций для определения значений коэффициентов.

    Выводятся корни уравнения.

    """
    a = choose('a')
    b = choose('b')
    c = choose('c')
    if a.__class__ is complex or b.__class__ is complex or c.__class__ is complex:
        d = pow(b, 2) - 4*a*c
        print("z\u2081 = {:1.2f}".format((-b-cmath.sqrt(d)) / (2*a)))
        print("z\u2082 = {:1.2f}".format((-b+cmath.sqrt(d)) / (2*a)))
    else:
        d = math.pow(b, 2) - 4*a*c
        if d > 0:
            print("x\u2081 = {:1.2f}".format((-b-math.sqrt(d)) / (2*a)))
            print("x\u2082 = {:1.2f}".format((-b+math.sqrt(d)) / (2*a)))
        elif d == 0:
            print("x\u2081,\u2082 = {:1.2f}".format((-b-math.sqrt(d)) / (2*a)))
        else:
            print("x\u2081,\u2082 = {:1.2f} \u00b1 {:1.2f}j".format(-b / (2*a),math.sqrt(abs(d)) / (2*a)))


if __name__ == "__main__":
    main()