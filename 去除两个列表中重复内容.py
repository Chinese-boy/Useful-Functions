def fdsame(lst1, lst2):
    try:
        return [a for a in lst1 for b in lst2 if a.lower() == b.lower()]
    except AttributeError:
        return [same for same in lst1 if same in lst2]
