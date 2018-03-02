def weight_choice(weight):
    """
    :param weight: list对应的权重序列
    :return:选取的值在原列表里的索引
    """
    t = random.randint(0, sum(weight) - 1)
    for i, val in enumerate(weight):
        t -= val
        if t < 0:
            return i

# all_list是需要用到的随机元素列表，number是结果的长度，
# tables是all_list等长的数值列表如all_list为['a','b','c']那么tables就为[7,4,1],这样子‘a’出现的几率最大，‘c’出现的几率最小


def make_random(all_lists,numbers,tables):
    list_a = all_lists
    res=''
    for i in range(0,numbers):
        if i<numbers:
            res+=all_lists[weight_choice(tables)]
    return res