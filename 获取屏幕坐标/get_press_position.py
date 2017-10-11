# -*- coding: utf-8 -*-
# 获取鼠标点击位置的坐标，保存到position.txt文件中，Ctrl+C结束
import pythoncom
import pyHook
import time
import os

STOP = 0

def onMouseEvent(event):
	global STOP
	# 监听鼠标事件
	if 'mouse left down' in event.MessageName:
		print "MessageName:", event.MessageName
		print "Message:", event.Message
		print "Position:", event.Position
		print "---"
 
		with open('position.txt','a') as f:
			f.write(str(event.Position)+'\n')
	elif 'mouse right up' in event.MessageName:
		STOP = 1
	return True


def get_position():
	position = {}

	p_keys = [
			'login',
			'password',
			'vcode',
			'change_vcode',
			'login_button',
			'vcode_pos'
			]

	if os.path.exists('position.txt'):
		with open('position.txt','r') as f:
			pos = [i.strip() for i in f.readlines()]
			print pos,len(pos)
		# 只去前八个坐标点
		if len(pos) >= 8:
			pos = pos[:8]
			for i in range(4):
				position[p_keys[i]] = eval(pos[i])
			position[p_keys[4]] = eval(pos[-1])

		# 左上角，右上角，左下角坐标
		p1,p2,p3 = map(eval,pos[4:7])	
		width = p2[0] - p1[0]
		height = p3[1] - p1[1]

		position['vcode_pos'] = (p1[0],p1[1],width,height)

	os.remove('position.txt')
	print position
	return position


def main():
	# 创建一个“钩子”管理对象
	hm = pyHook.HookManager()
	# 监听所有鼠标事件
	hm.MouseAll = onMouseEvent
	# 设置鼠标“钩子”
	hm.HookMouse()
 
	while True:
		if STOP == 1:
			get_position()
			break
		pythoncom.PumpWaitingMessages()

 
if __name__ == "__main__":
	main()