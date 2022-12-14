def summ(*args):
    return sum(args)


def main():
    string = input("Введите числа через запятую: ")
    if string.isspace() or string == '':
        print(summ())
    else:
        lst = string.split(',')
        n=0
        for i in lst:
            try:
                lst[n] = float(i)
                n+=1
            except ValueError:
                print(f"Введено не число на позиции {n+1}")
                main()
                return
        print("Сумма всех чисел: {:1.2f}".format(summ(*lst)))


if __name__ == "__main__":   
    main()

