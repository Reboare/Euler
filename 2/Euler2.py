def genFib():
    first = 1
    second = 2
    while True:
        yield second
        first, second = second, first+second

if __name__ == '__main__':
    sum = 0
    for n in genFib():
        if n % 2 == 0:
            sum += n
        if n>= 4000000:
            break
    print sum
