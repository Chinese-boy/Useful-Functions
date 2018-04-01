def bubble(list_data):
    l = len(list_data) - 2
    i = 0
    while (i < l):
        j = l
        while (j >= i):
            if (list_data[j] > list_data[j + 1]):
                list_data[j + 1], list_data[j] = list_data[j], list_data[j + 1]
            j -= 1
        i += 1
    return list_data