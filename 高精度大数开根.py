# 此为Python大神Jerry所编写，拒绝转载。
def big_sqrt(n):
    lst = []
    res = []
    while n > 0:
        lst.append(n % 100)
        n //= 100
    q = lst.pop()
    for a in range(9, -1, -1):
        if a * a <= q:
            break
    res.append(a)
    if lst:
        qq = lst.pop()
        remind = (q - a * a) * 100 + qq
    else:
        remind = (q - a * a) * 100
    while lst:
        for b in range(9, -1, -1):
            if (a * 20 + b) * b <= remind:
                break
        res.append(b)
        q = lst.pop()
        remind = (remind - (a * 20 + b) * b) * 100 + q
        a = int(''.join([str(i) for i in res]))
    return a
