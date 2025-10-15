def print_star_pattern(n):
    if n <= 0:
        print("NoPattern")
    else:
        for i in range(1, n + 1):
            print('|>' * i)
try:
    n = int(input())
    print_star_pattern(n)
except ValueError:
    print()