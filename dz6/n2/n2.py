def main():
    with open('n2/Input.txt', 'r') as file:
        string = file.read()
    lst = string.split(',')
    c = int(lst[0])
    h = int(lst[1])
    o = int(lst[2])
    m=0
    while True:
        if c >= 2 and h >=6 and o >=1:
            m+=1
            c-=2
            h-=6
            o-=1
        else:
            break
    with open('n2/Output.txt', 'w') as file:
        file.write(f'Из данного колличества атомов получится {m} молекул')


if __name__ == "__main__":
    main()