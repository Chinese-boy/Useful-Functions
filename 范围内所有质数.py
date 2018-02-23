def countPrimes(n):
    if n < 3: return 0
    res = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        res[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if res[i]]
