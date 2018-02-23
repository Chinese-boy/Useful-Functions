def flat(lst):
    return [x for sub in lst for x in flat(sub)] if isinstance(lst, (list, tuple)) else [lst]
