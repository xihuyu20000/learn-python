def replace(line, words_dict):
    """
    假设line是'aa;bb;cc;dd'，words_dict是{'aa':1,'cc':2}，返回值是1;bb;2;dd
    :param line:
    :param words_dict:
    :return:
    """
    keys = words_dict.keys()
    words = [str(words_dict[w]) if w in keys else w for w in line.split(';')]
    return ';'.join(words)


print(replace('aa;bb;cc;dd', {'aa':1,'cc':2}))