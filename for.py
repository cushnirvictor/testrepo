a, b, c, d = int(input('a= ')), int(input('b= ')), int(input('c= ')), int(input('d= '))
if a <= b and c <= d and a <= 10 and b <= 10 and c <= 10 and d <= 10:
    #print ('', end='')
    for j in range(c, d + 1):
        print('\t', j, end='')
    # print()
    for i in range(a, b + 1):
        print('\n', i, end='')
        for j in range(c, d + 1):
            print('\t', j * i, end='')
    # print()
