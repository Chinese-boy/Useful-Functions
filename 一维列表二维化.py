def rflat(lst):
    return list(zip(*[iter(lst)]*2))
