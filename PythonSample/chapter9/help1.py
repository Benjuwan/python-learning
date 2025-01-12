def prime(n):
    """引数が素数ならばTrueを返す。"""
    return n > 1 and all((n%i for i in range(2, n)))

help(prime)
