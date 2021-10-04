n = 0
while 0 <= n <= 1000:
    a = str(' Программист')
    if 10 < n % 100 < 15 or 10 < n < 15:
        b = 'ов'
    elif n == 1 or n % 10 == 1:
        b = ''
    elif 1 < n % 10 < 5 or 1 < n % 100 < 5:
        b = 'а'
    else:
        b = 'ов'
    print(str(n) + a + b)
    n += 1