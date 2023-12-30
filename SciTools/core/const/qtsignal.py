from PySide2 import QtCore


class MySignal(QtCore.QObject):
    info = QtCore.Signal(str)
    error = QtCore.Signal(str)
    set_clean_dataset = QtCore.Signal(object)
    datafiles_changing = QtCore.Signal()
    reset_cache = QtCore.Signal()
    push_cache = QtCore.Signal(str, object)
    update_cache = QtCore.Signal()


ssignal = MySignal()
