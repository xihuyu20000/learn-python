from core import Logger, OS


def test_Logger():
    Logger.debug('a', 'b')
    Logger.info('c', 'd')
    Logger.error('e', 'f')
    assert True

def test_os():
    name = OS.GetSystemVersionWindows()
    assert name.startswith('Windows')

def test_mem():
    value = OS.GetMemInfoWindows()
    assert value