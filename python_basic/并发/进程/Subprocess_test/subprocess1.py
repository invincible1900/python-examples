#coding:utf-8
import subprocess
import time


def start_craw():
    script = r'ping 192.168.1.1 -n 10'

    proc = subprocess.Popen(script)
    return proc
# t = threading.Thread(target=start_craw)
# t.start()
#
# while True:
#     time.sleep(2)
#     print ('main')
# returncode = subprocess.call(script)
p = start_craw()
while True:
    print p.poll()
    time.sleep(1)

