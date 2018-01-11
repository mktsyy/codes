##testmultiprocessing
#- * -coding: utf - 8 - * -


from multiprocessing import Process,Queue,Manager
import os
import time

##Python 进程之间共享数据 http://blog.csdn.net/houyanhua1/article/details/78244288
qq = ['1','2','3','4']


# 子进程要执行的代码
def run_proc(name,q):
	print q
	q.remove(q[0])
	print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
	q = Manager().list(qq)
	while True:
		time.sleep(1)
		print('Parent process %s.' % os.getpid())
		p = Process(target=run_proc, args=('test',q))
		p1 = Process(target=run_proc, args=('hello',q))
		print('Child process will start.')
		p.start()
		p1.start()
		p.join()
		p1.join()

		print q
		print('Child process end.')