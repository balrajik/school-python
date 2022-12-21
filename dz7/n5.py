import numpy


def main():
    n = numpy.random.random((3,3))
    print(f'массив 3x3 со случайными значениями:\n{n}')
    print(f'Транспонированный массив:\n{n.transpose()}')

if __name__ == "__main__":
    main()