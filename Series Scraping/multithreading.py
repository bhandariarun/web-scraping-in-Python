# import threading
# import time
#
# def count(f):
#     time.sleep(f)
#     print(f)
#
# # for i in range(10):
# #     x=threading.Thread(target=count,args=(i,))
# #     x.start()
#
#
# x=threading.Thread(target=count,args=(1,))
# x.start()
# x1=threading.Thread(target=count,args=(3,))
# x1.start()
# x2=threading.Thread(target=count,args=(5,))
# x2.start()
# x3=threading.Thread(target=count,args=(7,))
# x3.start()
#
# x.join()
# x1.join()
# x2.join()
# x3.join()
#
# print("completed")

x="hello"

def a():
    print(x)
    x=1

a()