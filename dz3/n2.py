from n1 import print_position


x = 0
y = 0


def move(direction, amount):
    """Перемещение

    Параметры:
        direction - направление.
        amount - количество шагов.

    Результат:
        Происходит перемещение персонажа и выводятся новые координаты
    """
    global x
    global y
    if direction == 'w':
        y += amount
        print_position(x, y)
    elif direction == 's':
        y -= amount
        print_position(x, y)
    elif direction == 'd':
        x += amount
        print_position(x, y)
    elif direction == 'a':
        x -= amount
        print_position(x, y)


def main():
    """Управление.

    Происходит выбор направления движения и количество шагов.

    Проводится вызов функции перемещения.
    """    
    while True:
        direction = input("Выберите направление (w - вверх, s - вниз, d - вправо, a - влево, e - прекратить движение): ")
        if direction in ['w', 'a', 's', 'd', 'e']:  
            if direction == 'e':
                break          
            else:
                amount = int(input("Выберите количество шагов: "))
                if amount > 0:
                    move(direction, amount)
                else:
                    print("Количество шагов должно быть больше нуля")
                    continue
        else:
            print("Неверный ввод")
            continue


if __name__ == "__main__":
    main()



