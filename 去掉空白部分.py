def pretty_space(file, encoding='utf-8'):
    from re import split as rsplit
    result = []
    with open(file, 'r', encoding=encoding) as f:
        for each_line in f:
            data = rsplit(r'\s+', each_line)
            while '' in data:
                data.remove('')
            result += data
    with open(file, 'w', encoding=encoding) as r:        
        r.write(' '.join(result).strip())