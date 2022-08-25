for i in range(1,10) :
    number = 1
    for j in range(1,10) :
        if i+j >= 10:
            print(number, end='')
            number = number+1
        else:
            print('-', end='')
    print()