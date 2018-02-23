def isinscope(start, stop, number, condition=True):
    return start < number < stop if condition else start <= number <= stop
