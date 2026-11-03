from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1 or n == 2:
        return n

    if n == 3:
        return f(2)

    if n > 3:
        return n * (f(n - 2) + f(n - 3))

    raise ValueError("n باید مثبت باشد")


print(f(7))