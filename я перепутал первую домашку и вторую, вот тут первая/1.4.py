def factorize(x):
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            print(i, x // i)
factorize(int(input()))
