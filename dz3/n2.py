x=0
y=0


def print_position():
    print("Положение персонажа: x - ({}), y - ({})".format(x,y))


def move(direction,amount):
    global x
    global y
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


def main():
    while True:
        direction = input("Выберите направление (w- вверх, s- вниз, d- вправо, a- влево, e - прекратить движение): ")
        if direction in ['w','a','s','d','e']:  
            if direction == 'e':
                break          
            else:
                amount = int(input("Выберите количество шагов: "))
                if amount > 0:
                    move(direction,amount)
                else:
                    print("Количество шагов должно быть больше нуля")
                    continue
        else:
            print("Неверный ввод")
            continue
        
                    
main()



