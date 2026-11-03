def DC(a, n):
    if n == 0:
        return 1

    if n < 0:
        return 1 / DC(a, -n)

    if n % 2 == 0:
        x = DC(a, n // 2)
        return x * x

    return a * DC(a, n - 1)


print(DC(2, 5))
print(DC(2, 8))
print(DC(3, 0))
print(DC(2, -3))