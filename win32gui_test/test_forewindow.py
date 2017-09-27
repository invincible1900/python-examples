# coding: utf-8
import re, traceback
import win32gui, win32con, win32com.client
from time import sleep
class cWindow:
    def __init__(self):
        self._hwnd = None
        self.shell = win32com.client.Dispatch("WScript.Shell")
        # print self.shell
    def BringToTop(self):
        win32gui.BringWindowToTop(self._hwnd)
    def SetAsForegroundWindow(self):
        self.shell.SendKeys('%')
        win32gui.SetForegroundWindow(self._hwnd)
    def Maximize(self):
        win32gui.ShowWindow(self._hwnd, win32con.SW_MAXIMIZE)
    def setActWin(self):
        win32gui.SetActiveWindow(self._hwnd)
    def _window_enum_callback(self, hwnd, wildcard):
        '''Pass to win32gui.EnumWindows() to check all the opened windows'''
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._hwnd = hwnd
    def find_window_wildcard(self, wildcard):
        self._hwnd = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def kill_task_manager(self):
        wildcard = 'Gestionnaire des t.+ches de Windows'
        # wildcard = ".*Sublime.*"
        
        self.find_window_wildcard(wildcard)
        if self._hwnd:
            win32gui.PostMessage(self._hwnd, win32con.WM_CLOSE, 0, 0)
            sleep(0.5)
def main():
    # sleep(5)
    try:
        # wildcard = ".*Building Operation WorkStation.*"
        wildcard = ".*Sublime.*"
        cW = cWindow()
        cW.kill_task_manager()
        cW.find_window_wildcard(wildcard)
        cW.BringToTop()
        # cW.Maximize()
        cW.SetAsForegroundWindow()
    except:
        f = open("log.txt", "w")
        f.write(traceback.format_exc())
        print(traceback.format_exc())
if __name__ == '__main__':
    while True:
        main()
