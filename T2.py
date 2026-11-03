def sum_recursive(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n باید عدد صحیح باشد")

    if n < 1:
        raise ValueError("n باید بزرگ‌تر یا مساوی 1 باشد")

    if n == 1:
        return 1

    return n + sum_recursive(n - 1)


print(sum_recursive(5))