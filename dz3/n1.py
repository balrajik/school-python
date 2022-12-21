def print_position(x, y):
    """Вывод положения.

    Параметры:
        x - положение персонажа по оси x.
        y - положение персонажа по оси y.

    В консоль выводится положение персонажа.
    """
    print("Положение персонажа: x - ({}), y - ({})".format(x, y))


def move():
    """Перемещение

    Происходит выбор направления движения и количество шагов

    Происходит перемещение персонажа
    """
    x = 0
    y = 0
    direction = input("Выберите направление (w- вверх, s- вниз, d- вправо, a- влево): ")
    if direction in ['w', 'a', 's', 'd']:
        amount = int(input("Выберите количество шагов: "))
        if amount > 0:
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
        else:
            print("Количество шагов должно быть больше нуля")
            move()
    else:
        print("Неверный ввод")
        move()

        
if __name__ == "__main__":
    move()
    