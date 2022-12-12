from n1 import generate_list


def main():
    set1 = set()
    set2 = set()
    set1.update(generate_list())
    set2.update(generate_list())
    print(f"Первый набор: {set1}")
    print(f"Второй набор: {set2}")
    print(f"Входят одновременно в оба: {get_intersection(set1,set2)}")
    print(f"Входят в первый, но не входят во второй: {get_difference(set1,set2)}")
    print(f"Входят во второй, но не входят в первый: {get_difference(set2,set1)}")
    print(f"Входят в первое или во второе, но не в оба из них одновременно: {get_symmetric_difference(set1,set2)}")


def get_intersection(s1,s2):
    if s1.intersection(s2):
        return s1.intersection(s2)
    else:
        return "Таких чисел нет"



def get_difference(s1,s2):  
    if s1-s2:
        return s1-s2
    else:
        return "Таких чисел нет"


def get_symmetric_difference(s1,s2):
    if s1.symmetric_difference(s2):
        return s1.symmetric_difference(s2)
    else:
        return "Таких чисел нет"



if __name__ == "__main__":
    main()