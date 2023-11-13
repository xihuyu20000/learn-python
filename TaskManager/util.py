import os
# import win32api
import win32gui
import win32process
from ctypes import *


# 列出系统当前所有进程。
def getProcessList():
    os.system("tasklist")



# 结构体
class THREADENTRY32(Structure):
    _fields_ = [('dwSize', c_ulong),
                ('cntUsage', c_ulong),
                ('th32ThreadID', c_ulong),
                ('th32OwnerProcessID', c_ulong),
                ('tpBasePri', c_long),
                ('tpDeltaPri', c_long),
                ('dwFlags', c_ulong)]


# 获取指定进程的所有线程
def getThreadOfProcess(pid):
    dll = windll.LoadLibrary("KERNEL32.DLL")
    snapshotHandle = dll.CreateToolhelp32Snapshot(0x00000004, pid)
    struct = THREADENTRY32()
    struct.dwSize = sizeof(THREADENTRY32)
    flag = dll.Thread32First(snapshotHandle, byref(struct))

    while flag != 0:
        if (struct.th32OwnerProcessID == int(pid)):
            print("线程id：" + str(struct.th32ThreadID))
        flag = dll.Thread32Next(snapshotHandle, byref(struct))
    dll.CloseHandle(snapshotHandle)


# EnumWindows的回调函数
def callback(hwnd, windows):
    pidList = win32process.GetWindowThreadProcessId(hwnd)
    for pid in pidList:
        windows.setdefault(pid, [])
        windows[pid].append(hwnd)


# 显示和隐藏指定进程的窗口
def changeWindowState(pid, status):
    windows = {}
    win32gui.EnumWindows(callback, windows)
    try:
        hwndList = windows[int(pid)]
        # 显示/隐藏窗口
        for hwnd in hwndList:
            win32gui.ShowWindow(hwnd, int(status))
    except:
        print("进程不存在")


# 强行结束指定进程
def killProcess(pid):
    cmd = 'taskkill /pid ' + pid + ' /f'
    try:
        os.system(cmd)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    while (True):
        print()
        print()
        print("************************************")
        print("*                                  *")
        print("*     进程管理器                   *")
        print("*                                  *")
        print("*     1.获取所有进程               *")
        print("*     2.获取指定进程的所有线程     *")
        print("*     3.显示和隐藏指定进程的窗口   *")
        print("*     4.强行结束指定进程           *")
        print("*                                  *")
        print("************************************")
        option = input("请选择功能：")

        if option == "1":
            getProcessList()
        elif option == "2":
            pid = input("请输入进程的pid：")
            getThreadOfProcess(pid)
        elif option == "3":
            pid = input("请输入进程的pid：")
            status = input("隐藏输入0，显示输入1：")
            changeWindowState(pid, status)
        elif option == "4":
            pid = input("请输入进程的pid：")
            killProcess(pid)
        else:
            exit()