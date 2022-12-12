import random


def main():
    L = generate_list()
    print(f"Несортированный список: {L}")
    print(f"Соритрованный список: {bubblesort(L)}")


def generate_list():
        l = []
        for i in range(10):
            l.append(random.randint(1,50))
        return l

def bubblesort(list):
    for i in range(len(list)-1):
        for j in range (len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


if __name__ == "__main__":
    main()


