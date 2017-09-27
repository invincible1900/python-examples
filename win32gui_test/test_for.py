#coding:utf-8
import re
import win32gui, win32con, win32com.client
from time import sleep
import threading
import time
STOP = 0

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

    # def setActWin(self):
    #     win32gui.SetActiveWindow(self._hwnd)


    def _window_enum_callback(self, hwnd, wildcard):
        '''Pass to win32gui.EnumWindows() to check all the opened windows'''
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
			print wildcard
			print str(win32gui.GetWindowText(hwnd))
			self._hwnd = hwnd
			print hwnd

    def find_window_wildcard(self, wildcard):
        self._hwnd = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

def main(wildcard):
	wildcard = ".*python.*"
	cW = cWindow()
	cW.find_window_wildcard(wildcard)
	cW.Maximize()
	cW.BringToTop()
	cW.SetAsForegroundWindow()

if __name__ == '__main__':
	titles = set()
	def foo(hwnd,mouse):
		#去掉下面这句就所有都输出了，但是我不需要那么多
		if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
			titles.add(win32gui.GetWindowText(hwnd))

	win32gui.EnumWindows(foo, 0)
	lt = [t for t in titles if t]
	lt.sort()

	print 'Running windows:'
	for t in lt:
		print t

	wildcard = ''
	while not wildcard:
		wildcard = raw_input('input target window name:')

	main(wildcard)
	
	

# from win32gui import *
