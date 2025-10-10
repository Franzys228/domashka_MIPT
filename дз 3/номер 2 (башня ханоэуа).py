def hanoi_tower(a, b, c, n):
    if n > 0:
        hanoi_tower(a, c, b, n - 1)
        print(a, '->', b)
        hanoi_tower(c, b, a, n - 1)
