def num_fibonacci(num):
    """Числа Фибоначчи

    Параметры:
        num - номер числа в последовательности.
    
    Возвращает: 
        Число с заданным номером
    """
    if num == 1:
        return 0
    if num == 2: 
        return 1
    else:
        return num_fibonacci(num - 2) + num_fibonacci(num - 1)



def main():
    """
    Вводится номер числа Фибоначчи и выводится значение заданного числа.
    """
    try:
        num = int(input("Введите номер числа Фибоначчи: "))
    except ValueError:
        print("Неверный ввод")
    print(num_fibonacci(num))


if __name__ == "__main__":
    main()

