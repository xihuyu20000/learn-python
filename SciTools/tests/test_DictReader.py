from core.util.mutil import DictReader


def test_combine_words_file():
    words_dict = DictReader.combine_words_file(r"..\dicts\合并词表.txt")
    print('\r\n')
    print(words_dict)
    assert len(words_dict)>0
def test_stop_words_file():
    words_set = DictReader.stop_words_file(r"..\dicts\停用词表.txt")
    print('\r\n')
    print(words_set)
    assert len(words_set)>0
def test_controlled_words_file():
    words_set = DictReader.controlled_words_file(r"..\dicts\受控词表.txt")
    print('\r\n')
    print(words_set)
    assert len(words_set)>0