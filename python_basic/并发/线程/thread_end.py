# import time
# import threading
#
#
# def f1():
#     while True:
#         # print('f1')
#         time.sleep(5)
#
# def main():
#     for i in range(10):
#         t = threading.Thread(target=f1)
#         t.setDaemon(True)
#         t.start()
#
# if __name__ == '__main__':
#     for _ in range(10):
#         t = threading.Thread(target=main)
#         t.start()
#         t.join()
#         print('current threads:', threading.active_count())
#         # for t in threading.enumerate():
#         #     print(t.name, t.is_alive())
#
