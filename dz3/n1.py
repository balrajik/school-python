x=0
y=0


def print_position():
    print("Положение персонажа: x - ({}), y - ({})".format(x,y))


def move():
    global x
    global y
    direction = input("Выберите направление (w- вверх, s- вниз, d- вправо, a- влево): ")
    if direction in ['w','a','s','d']:
        amount = int(input("Выберите количество шагов: "))
        if amount > 0:
            if direction == 'w':
                y += amount
                print_position()
            elif direction == 's':
                y -= amount
                print_position()
            elif direction == 'd':
                x += amount
                print_position()
            elif direction == 'a':
                x -= amount
                print_position()
        else:
            print("Количество шагов должно быть больше нуля")
            move()
    else:
        print("Неверный ввод")
        move()

        
move()