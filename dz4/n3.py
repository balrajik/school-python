from n1 import generate_list


def main():
    """
    Выводит пересечение,разницу и симметрическую разницу двух случайно сгенерированных сэта.
    """
    set1 = set()
    set2 = set()
    set1.update(generate_list())
    set2.update(generate_list())
    print(f"Первый набор: {set1}")
    print(f"Второй набор: {set2}")
    print(f"Входят одновременно в оба: {get_intersection(set1, set2)}")
    print(f"Входят в первый, но не входят во второй: {get_difference(set1, set2)}")
    print(f"Входят во второй, но не входят в первый: {get_difference(set2, set1)}")
    print(f"Входят в первое или во второе, но не в оба из них одновременно: {get_symmetric_difference(set1, set2)}")


def get_intersection(s1, s2):
    """Пересечение
    
    Параметры:
        s1 - первый сэт
        s2 - второй сэт
    
    Возвращает:
        Числа, которые входят одновременно в оба сэта.
    """
    if s1.intersection(s2):
        return s1.intersection(s2)
    else:
        return "Таких чисел нет"



def get_difference(s1, s2):  
    """Разница
    
    Параметры:
        s1 - первый сэт
        s2 - второй сэт
    
    Возвращает:
        Числа, которые входят только в первое, но не входят во второе.
    """
    if s1 - s2:
        return s1 - s2
    else:
        return "Таких чисел нет"


def get_symmetric_difference(s1, s2):
    """Симметричная разница
    Параметры:
        s1 - первый сэт
        s2 - второй сэт
    
    Возвращает:
        Числа, которые входят в первое или во второе, но не в оба из них одновременно.
    """
    if s1.symmetric_difference(s2):
        return s1.symmetric_difference(s2)
    else:
        return "Таких чисел нет"



if __name__ == "__main__":
    main()