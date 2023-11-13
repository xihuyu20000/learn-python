import sys
import traceback
import datetime


def getnowtime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _log(content, level, *args):
    sys.stdout.write("%s - %s - %s\n" % (getnowtime(), level, content))
    for arg in args:
        sys.stdout.write("%s\n" % arg)


def debug(content, *args):
    _log(content, 'DEBUG', *args)


def info(content, *args):
    _log(content, 'INFO', *args)


def warn(content, *args):
    _log(content, 'WARN', *args)


def error(content, *args):
    _log(content, 'ERROR', *args)


def exception(content):
    sys.stdout.write("%s - %s\n" % (getnowtime(), content))
    traceback.print_exc(file=sys.stdout)
