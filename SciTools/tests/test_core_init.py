from core import Logger, OS


def test_Logger():
    Logger.debug('ab')
    Logger.info('cd')
    Logger.error('ef')
    assert True

def test_os():
    name = OS.GetSystemVersionWindows()
    assert name.startswith('Windows')

def test_mem():
    value = OS.GetMemInfoWindows()
    assert value