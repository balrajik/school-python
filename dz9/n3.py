def num_fibonacci(num):
    if num == 1:
        return 0
    if num == 2: 
        return 1
    else:
        return num_fibonacci(num - 2) + num_fibonacci(num - 1)