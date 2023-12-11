from mhelper import Cfg


def replace2(line, words_set):
    words = [w for w in line.split(';') if w not in words_set]
    print(words)
    return ';'.join(words)

print(replace2('aa;bb;cc;dd', ['aa','bb']))